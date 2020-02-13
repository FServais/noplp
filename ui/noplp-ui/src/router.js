import VueRouter from 'vue-router';

const routes = [
  {
    name: 'home',
    path: '/',
    component: require('./components/Home.vue').default,
  },
  {
    name: 'round',
    path: '/round/:roundid',
    component: require('./components/Round.vue').default,
  },
  {
    name: 'category',
    path: '/category/:category/level/:level',
    component: require('./components/Category.vue').default,
  },
  {
    name: 'song',
    path: '/song/artist/:artist/title/:title/level/:level',
    component: require('./components/Song.vue').default,
  },
  {
    name: 'adminsong',
    path: '/admin/song/:challengeid',
    component: require('./components/AdminSong.vue').default,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
