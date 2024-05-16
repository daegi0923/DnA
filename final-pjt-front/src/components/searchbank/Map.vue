<template>
    <div>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
      <div class="container">
        <div class="row">
          <div class="col-md-6 offset-md-3">
            <div class="input-group mb-3">
              <input type="text" class="form-control search-input" v-model="keyword" placeholder="장소를 검색하세요" @keyup.enter="searchPlaces">
              <div class="input-group-append">
                <button class="btn btn-primary search-button" type="button" @click="searchPlaces">검색</button>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div id="map"></div>
      <div>
        <div id="menu_wrap" class="container">
          <ul class="list-group">
            <li v-for="(place, index) in places" :key="index" class="list-group-item custom-list-item" :class="'marker_' + (index + 1)">
              <span class="markerbg"></span>
              <div class="info">
                <h5>{{ place.place_name }}</h5>
                <span>{{ place.road_address_name ? place.road_address_name : place.address_name }}</span>
                <span class="tel">{{ place.phone }}</span>
              </div>
            </li>
          </ul>
        </div>
  
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "KakaoMap",
    data() {
      return {
        map: null,
        keyword: "",
        places: [],
        markers: [],
      };
    },
    created() {},
    mounted() {
      if (window.kakao && window.kakao.maps) {
        this.loadMap();
      } else {
        this.loadScript();
      }
    },
    methods: {
      
      loadScript() {
        const script = document.createElement("script");
        script.src =
          "//dapi.kakao.com/v2/maps/sdk.js?appkey=fb46c88703e2ee3761ca6cee1048de3c&libraries=services&autoload=false";
        script.onload = () => window.kakao.maps.load(() => this.loadMap());
        document.head.appendChild(script);
      },
      loadMap() {
        const container = document.getElementById("map");
        const options = {
          center: new window.kakao.maps.LatLng(33.450701, 126.570667),
          level: 3,
        };
        this.map = new window.kakao.maps.Map(container, options);
      },
      loadMarker() {
        const markerPosition = new window.kakao.maps.LatLng(33.450701, 126.570667);
        const marker = new window.kakao.maps.Marker({
          position: markerPosition,
        });
        marker.setMap(this.map);
      },
      searchPlaces() {
        let keyword = this.keyword.trim();
        keyword += ' 은행'
        if (!keyword) {
          alert("키워드를 입력해주세요!");
          return false;
        }
        const ps = new window.kakao.maps.services.Places();
        ps.keywordSearch(keyword, this.placesSearchCB);
      },
      placesSearchCB(data, status, pagination) {
        if (status === window.kakao.maps.services.Status.OK) {
          this.places = data;
          this.displayPlaces(data);
          this.displayPagination(pagination);
        } else if (status === window.kakao.maps.services.Status.ZERO_RESULT) {
          alert("검색 결과가 존재하지 않습니다.");
          this.places = [];
        } else if (status === window.kakao.maps.services.Status.ERROR) {
          alert("검색 결과 중 오류가 발생했습니다.");
          this.places = [];
        }
      },
      displayPlaces(places) {
        const listEl = document.getElementById("placesList");
        const menuEl = document.getElementById("menu_wrap");
        const fragment = document.createDocumentFragment();
        const bounds = new window.kakao.maps.LatLngBounds();
        let listStr = '';
        if (listEl) {
          this.removeAllChildNods(listEl);
          this.removeMarker();
        }
        for (let i = 0; i < places.length; i++) {
          const place = places[i];
          const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
          const marker = this.addMarker(placePosition, i, place.place_name);
          const itemEl = this.getListItem(i, place);
          const infowindow = new window.kakao.maps.InfoWindow({
            zIndex: 1,
          });
  
          bounds.extend(placePosition);
  
          (function(marker, title) {
            window.kakao.maps.event.addListener(marker, "mouseover", function() {
              infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
              infowindow.open(this.map, marker);
            });
  
            window.kakao.maps.event.addListener(marker, "mouseout", function() {
              infowindow.close();
            });
  
            itemEl.onmouseover = function() {
              infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
              infowindow.open(this.map, marker);
            };
  
            itemEl.onmouseout = function() {
              infowindow.close();
            };
          })(marker, place.place_name);
  
          fragment.appendChild(itemEl);
        }
  
        // listEl.appendChild(fragment);
        menuEl.scrollTop = 0;
  
        this.map.setBounds(bounds);
      },
      getListItem(index, place) {
        const el = document.createElement("li");
        let itemStr = '<span class="markerbg marker_' + (index + 1) + '"></span>' +
          '<div class="info">' +
          '   <h5>' + place.place_name + '</h5>';
  
        if (place.road_address_name) {
          itemStr +=
            '    <span>' + place.road_address_name + '</span>' +
            '   <span class="jibun gray">' + place.address_name + '</span>';
        } else {
          itemStr += '    <span>' + place.address_name + '</span>';
        }
  
        itemStr += '  <span class="tel">' + place.phone + '</span>' +
          '</div>';
  
        el.innerHTML = itemStr;
        el.className = "item";
  
        return el;
      },
      addMarker(position, idx, title) {
        const imageSrc =
          "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
        const imageSize = new window.kakao.maps.Size(36, 37);
        const imgOptions = {
          spriteSize: new window.kakao.maps.Size(36, 691),
          spriteOrigin: new window.kakao.maps.Point(0, idx * 46 + 10),
          offset: new window.kakao.maps.Point(13, 37),
        };
        const markerImage = new window.kakao.maps.MarkerImage(
          imageSrc,
          imageSize,
          imgOptions
        );
        const marker = new window.kakao.maps.Marker({
          position: position,
          image: markerImage,
        });
  
        marker.setMap(this.map);
        this.markers.push(marker);
  
        return marker;
      },
      removeMarker() {
        for (let i = 0; i < this.markers.length; i++) {
          this.markers[i].setMap(null);
        }
        this.markers = [];
      },
      displayPagination(pagination) {
        if (this.listEl && this.listEl.hasChildNodes()) {
          const paginationEl = document.getElementById("pagination");
          const fragment = document.createDocumentFragment();
  
          while (paginationEl.hasChildNodes()) {
            paginationEl.removeChild(paginationEl.lastChild);
          }
  
          for (let i = 1; i <= pagination.last; i++) {
            const el = document.createElement("a");
            el.href = "#";
            el.innerHTML = i;
  
            if (i === pagination.current) {
              el.className = "on";
            } else {
              el.onclick = (function(i) {
                return function() {
                  pagination.gotoPage(i);
                };
              })(i);
            }
  
            fragment.appendChild(el);
          }
          paginationEl.appendChild(fragment);
        }
      },
      displayInfowindow(marker, title) {
        const content = '<div style="padding:5px;z-index:1;">' + title + "</div>";
  
        infowindow.setContent(content);
        infowindow.open(this.map, marker);
      },
      removeAllChildNods(el) {
        while (el.hasChildNodes()) {
          el.removeChild(el.lastChild);
        }
      },
    },
  };
  </script>
  
<style scoped>
#map {
width: 100%;
height: 1000px;
}

.custom-list-item {
    margin: 10px;
}
.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
</style>