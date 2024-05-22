<template>
    <div class="container">
      <div class="container">
  <div class="row">
    <div class="col-md-6">
      <v-text-field
        variant="outlined"
        v-model="keyword"
        label="키워드나 장소를 검색하세요"
        append-inner-icon="mdi-magnify"
        @click:append-inner="searchPlaces"
        @keyup.enter="searchPlaces"
        outlined
        dense
      ></v-text-field>
    </div>
    <div class="col-md-6">
      <form @submit.prevent="clickPlaces" class="d-flex">
        <v-select
          variant="outlined"
          v-model="province"
          :items="provinces"
          label="도/광역시/특별시"
          outlined
          dense
          class="mr-2"
        ></v-select>
        <v-select
          variant="outlined"
          v-model="city"
          :items="cities[province]"
          label="시/군/구"
          outlined
          dense
          class="mr-2"
        ></v-select>
        <v-text-field
          variant="outlined"
          v-model="bank"
          label="은행명"
          dense
          class="mr-2"
        ></v-text-field>
        <v-btn type="submit" color="primary" class="mt-2"><font-awesome-icon :icon="['fas', 'magnifying-glass']" /></v-btn>
      </form>
    </div>
  </div>
</div>
      <div id="map">
        <div id="menu_wrap" class="container">
          <v-list>
            <v-list-item
            v-for="(place, index) in places"
            :key="index"
            :class="'marker_' + (index + 1)"
          >
            <v-list-item-icon>
              <v-icon>mdi-map-marker</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ place.place_name }}</v-list-item-title>
              <v-list-item-subtitle>{{
                place.road_address_name
                  ? place.road_address_name
                  : place.address_name
              }}</v-list-item-subtitle>
              <v-list-item-subtitle>{{ place.phone }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
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
        province: "",
        city: "",
        bank: "",
        provinces: [
          '전체',
        '서울특별시',
        '인천광역시',
        '대전광역시',
        '대구광역시',
        '광주광역시',
        '부산광역시',
        '울산광역시',
        '세종특별자치시',
        '경기도',
        '강원도',
        '충청북도',
        '충청남도',
        '경상북도',
        '경상남도',
        '전라북도',
        '전라남도',
        '제주특별자치도',
        ],
        cities: {
          '전체': ['전체'],
          '서울특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
          '인천광역시': ['강화군', '계양구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구', '남동구'],
          '대전광역시': ['대덕구', '동구', '서구', '유성구', '중구'],
          '대구광역시': ['군위군', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
          '광주광역시': ['광산구', '남구', '동구', '북구', '서구'],
          '부산광역시': ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '영도구', '중구', '해운대구', '연제구'],
          '울산광역시': ['남구', '동구', '북구', '울주군', '중구'],
          '세종특별자치시': ['세종시'],
          '경기도': ['가평군', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '화성시'],
          '강원도': ['강릉시', '고성군', '동해시', '삼척시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '화천군', '횡성군', '속초시', '홍천군'],
          '충청북도': ['괴산군', '단양군', '보은군', '영동군', '옥천군', '증평군', '진천군', '청주시', '충주시', '제천시'],
          '충청남도': ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시', '청양군', '태안군', '홍성군'],
          '경상북도': ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시'],
          '경상남도': ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시', '통영시', '하동군', '함안군', '함양군', '합천군'],
          '전라북도': ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '익산시', '임실군', '전주시', '정읍시', '진안군', '장수군', '완주군'],
          '전라남도': ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '무안군', '목포시', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'],
          '제주특별자치도': ['제주시', '서귀포시'],
        },
      };
    },
    mounted() {
      if (window.kakao && window.kakao.maps) {
        this.loadMap();
      } else {
        this.loadScript();
      }
    },
    methods: {

      loadScript() {
        const API_KEY = import.meta.env.VITE_API_KEY;
        const script = document.createElement("script");
        script.src =
          `//dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&libraries=services&autoload=false`;
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
      clickPlaces() {
        let keyword = `${this.province} ${this.city} ${this.bank}`;
        const ps = new window.kakao.maps.services.Places();
        ps.keywordSearch(keyword, this.placesSearchCB)
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
  height: 750px;
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  font-family: "Nanum Gothic Coding", monospace;
  font-weight: 400;
  margin-bottom: 20px;
}

.custom-list-item {
    margin: 10px;
}
.map_wrap, .map_wrap * {
  margin: 0;
  padding: 0;
  font-family: 'Malgun Gothic', dotum, '돋움', sans-serif;
  font-size: 12px;
}

.map_wrap a, .map_wrap a:hover, .map_wrap a:active {
  color: #000;
  text-decoration: none;
}

.map_wrap {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0; /* 지도 아래에 위치하도록 설정합니다. */
  overflow: auto; /* 지도 영역을 벗어나도록 설정합니다. */
}


#menu_wrap {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 300px;
  height: calc(100% - 20px);
  padding: 5px;
  overflow-y: auto;
  background: rgba(255, 255, 255, 0.7);
  z-index: 100;
  font-size: 12px;
  border-radius: 10px;
}

#menu_wrap hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 2px solid #5F5F5F;
  margin: 3px 0;
}

#menu_wrap .option {
  text-align: center;
}

#menu_wrap .option p {
  margin: 10px 0;
}

#menu_wrap .option button {
  margin-left: 5px;
}

.map-form{
  display: flex;
  gap: 10px
}
</style>