<script setup>
import { reactive, inject, ref } from 'vue';
const imgSrc = reactive({
    Age: "",
    LAge: "",
    Gender: "",
    LGender: "",
    Education: "",
    LEducation: "",
    Ethnicity: ""
});

const country = inject("chooseCountry");
const counList = {
    "China": "CHN",
    "United States": "USA",
    "United Kingdom": "UK",
    "Australia": "Australia",
    "South Africa": "South_africa",
    "Germany": "Germany",
    "Japan": "Japan",
    "Israel": "Israel",
    "Hong Kong SAR": "HK",
    "France": "France",
    "Spain": "Spain",
    "Mexico": "Mexico",
    "Chile": "Chile",
    "Portugal": "Portugal",
    "Brazil": "Brazil",
    "Russian Federation": "Russia",
    "Egypt": "Egypt",
    "Qatar": "Qatar",
    "India": "India"
};
const useCountry = ref("");
useCountry.value = counList[country.value];

import(`../../../../assets/data/Study3/${useCountry.value}/demographics/${useCountry.value}_age.png`)
    .then(r => r.default)
    .then(r => imgSrc.Age = r);
import(`../../../../assets/data/Study3/${useCountry.value}/demographics/${useCountry.value}_education.png`)
    .then(r => r.default)
    .then(r => imgSrc.Education = r);
import(`../../../../assets/data/Study3/${useCountry.value}/demographics/${useCountry.value}_gender.png`)
    .then(r => r.default)
    .then(r => imgSrc.Gender = r);
import('../../../../assets/data/Study3/legend/study3_details_demographics_age.png')
    .then(r => r.default)
    .then(r => imgSrc.LAge = r);
import('../../../../assets/data/Study3/legend/study3_details_demographics_gender.png')
    .then(r => r.default)
    .then(r => imgSrc.LGender = r);
import('../../../../assets/data/Study3/legend/study3_details_demographics_education.png')
    .then(r => r.default)
    .then(r => imgSrc.LEducation = r);
import(`../../../../assets/data/Study3/${useCountry.value}/demographics/${useCountry.value}_ethnicity.png`)
    .then(r => r.default)
    .then(r => imgSrc.Ethnicity = r);
</script>

<template>
    <div class="alert-regio-demographics">
        <div>
            We collected age, gender, education, ethnicity in each region.
        </div>
        <div class="img-box">
            <div>
                <div>Age</div>
                <div class="im im-1" :style="`background-image: url(${imgSrc.Age}), url(${imgSrc.LAge});`"></div>
            </div>
            <div>
                <div>Gender</div>
                <div class="im im-2" :style="`background-image: url(${imgSrc.Gender}), url(${imgSrc.LGender});`"></div>
            </div>
            <div>
                <div>Education</div>
                <div class="im im-3" :style="`background-image: url(${imgSrc.Education}), url(${imgSrc.LEducation});`"></div>
            </div>
            <div style="height: 230px;">
                <div>Ethnicity</div>
                <div class="im im-4" :style="`background-image: url(${imgSrc.Ethnicity});`"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.img-box {
    display: flex;
    width: 100%;
    justify-content: space-between;
    margin: 20px 0 0 0;
    flex-wrap: wrap;
    text-align: center;
}

.img-box>div {
    width: 220px;
    height: 328px;
}
.img-box>div>div:nth-child(1) {
    font-weight: 600;
}
.img-box>div>div.im {
    display: inline-block;
    width: 100%;
    height: calc(100% - 24px);
    background-repeat: no-repeat;
}
.im-1 {
    background-size: 120px 324px, 82px 304px;
    background-position: 0px -10px, 124px 0px;
}
.im-2 {
    background-size: 110px 304px, 110px 96px;
    background-position: 0px 0px, 110px 104px;
}
.im-3 {
    background-size: 110px 304px, 110px 304px;
    background-position: 0px 0px, 110px 0px;
}
.im-4 {
    background-size: 220px 220px;
    background-position: 0px 0px;
}

@media screen and (max-width: 600px) {
    .img-box {
        justify-content: center;
    }
}
</style>
