import { createRouter, createWebHashHistory } from "vue-router";
import Home from '../views/Home.vue';
import Favee from '../views/home/FAVEE.vue';
import f3d from '../views/home/favee3d.vue';
import Study1 from '../views/home/Study1.vue';
import Study2 from '../views/home/Study2.vue';
import Study3 from '../views/home/Study3.vue';
import region from '../views/home/region.vue';

import alert3D from '../views/alert/modelDetails.vue';
import alertDemographics from '../views/alert/demographics.vue';
import alertCultural from '../views/alert/cultural.vue';
import alertRelationship from '../views/alert/relationship.vue';
import alertStudy1 from '../views/alert/study1.vue';
import alertStudy2 from '../views/alert/study2.vue';
import alertSubset from '../views/alert/subset.vue';
import alertRegion from '../views/alert/region.vue';

const routes = [
    { 
        path: "/",
        components: {
            default: Home,
            Favee,
            f3d,
            Study1,
            Study2,
            Study3,
            region,
            alert3D,
            alertDemographics,
            alertCultural,
            alertRelationship,
            alertStudy1,
            alertStudy2,
            alertSubset,
            alertRegion
        }
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router