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
            <v-btn type="submit" color="primary" class="mt-2">
              <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
            </v-btn>
          </form>
        </div>
      </div>
    </div>
    <div class="map-container">
      <div id="map"></div>
      <v-btn @click="goToCurrentLocation" color="#3F72AF" class="current-location-btn"><font-awesome-icon :icon="['fas', 'location-crosshairs']" /></v-btn>
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
        '전체', '서울특별시', '인천광역시', '대전광역시', '대구광역시', '광주광역시', '부산광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '경상북도', '경상남도', '전라북도', '전라남도', '제주특별자치도',
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
      script.onload = () => window.kakao.maps.load(this.loadMap);
      document.head.appendChild(script);
    },
    loadMap() {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(37.5665, 126.9780),
        level: 3,
      };
      this.map = new kakao.maps.Map(container, options);
    },
    searchPlaces() {
      if (!this.keyword.trim()) {
        alert("키워드를 입력해주세요!");
        return;
      }
      const places = new kakao.maps.services.Places();
      places.keywordSearch(this.keyword, this.placesSearchCB);
    },
    placesSearchCB(data, status) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 없습니다.");
      } else {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },
    displayPlaces(places) {
      this.clearMarkers();
      const bounds = new kakao.maps.LatLngBounds();

      for (const place of places) {
        console.log(place);
        const markerPosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = new kakao.maps.Marker({
          position: markerPosition,
        });
        
        const infoWindow = new kakao.maps.InfoWindow({
          content: `<div style="padding:5px;">${place.place_name}</div>`,
        });

        marker.setClickable(true); // Enable click event for marker
        kakao.maps.event.addListener(marker, 'click', () => {
          window.open(place.place_url, '_blank');
        });

        kakao.maps.event.addListener(marker, 'mouseover', () => {
          infoWindow.open(this.map, marker);
        });

        kakao.maps.event.addListener(marker, 'mouseout', () => {
          infoWindow.close();
        });

        marker.setMap(this.map);
        this.markers.push(marker);
        bounds.extend(markerPosition);
      }

      this.map.setBounds(bounds);
    },
    clearMarkers() {
      for (const marker of this.markers) {
        marker.setMap(null);
      }
      this.markers = [];
    },
    clickPlaces() {
      if (!this.province || !this.city || !this.bank) {
        alert("모든 필드를 입력해주세요!");
        return;
      }
      const query = `${this.province} ${this.city} ${this.bank} 은행`;
      const places = new kakao.maps.services.Places();
      places.keywordSearch(query, this.placesSearchCB);
    },
    goToCurrentLocation() {
      if (navigator.geolocation) {
        // 현재 위치를 가져옵니다.
        navigator.geolocation.getCurrentPosition(
          position => {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            const currentLocation = new kakao.maps.LatLng(lat, lng);
            
            // 현재 위치로 지도를 이동합니다.
            this.map.setCenter(currentLocation);
          },
          error => {
            console.error("현위치를 가져오는데 문제가 발생했습니다:", error);
            alert("현위치를 가져오는데 문제가 발생했습니다.");
          }
        );
      } else {
        console.error("현위치를 가져오는데 문제가 발생했습니다: 브라우저가 Geolocation API를 지원하지 않습니다.");
        alert("현위치를 가져오는데 문제가 발생했습니다: 브라우저가 Geolocation API를 지원하지 않습니다.");
      }
  },
}
};
</script>
<style scoped>
#map {
  width: 100%;
  height: 720px;
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

.map-form{
  display: flex;
  gap: 10px
}

.custom-infowindow {
  z-index: 100; /* Ensure infoWindow is on top */
}

.current-location-btn {
  width: 5px;
  position: absolute;
  bottom: 50px;
  right: 200px;
  z-index: 100;
}

</style>