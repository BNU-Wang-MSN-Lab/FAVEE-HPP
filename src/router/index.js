import { createRouter, createWebHashHistory } from "vue-router";
import Home from '../views/Home.vue';

import Page1 from '../views/Page1.vue';
import Page2 from '../views/Page2.vue';
import Page3 from '../views/Page3.vue';
import Page4 from '../views/Page4.vue';
import Page5 from '../views/Page5.vue';
import Page6 from '../views/Page6.vue';
import Page7 from '../views/Page7.vue';

import alertStudy1 from '../views/alert/study1.vue';
import alertStudy2 from '../views/alert/study2.vue';
import alertStudy3 from '../views/alert/study3.vue';
import alertDemographics from '../views/alert/demographics.vue';
import alertRegion from '../views/alert/region.vue';
import alertSubset from '../views/alert/subset.vue';
import alertCultural from '../views/alert/cultural.vue';
import alertRelationship from '../views/alert/relationship.vue';

const routes = [
    { 
        path: "/",
        components: {
            default: Home,
            Page1,
            Page2,
            Page3,
            Page4,
            Page5,
            Page6,
            Page7,
            alertStudy1,
            alertStudy2,
            alertStudy3,
            alertDemographics,
            alertSubset,
            alertCultural,
            alertRelationship,
            alertRegion
        }
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router