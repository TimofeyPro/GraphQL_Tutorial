// import Vue from 'vue'
// import VueRouter from 'vue-router'
import { createRouter, createWebHistory } from 'vue-router'

import Post from '@/components/Post'
import Author from '@/components/Author'
import PostsByTag from '@/components/PostsByTag'
import AllPosts from '@/components/AllPosts'

//Vue.use(VueRouter)

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/author/:username', component: Author },
    { path: '/post/:slug', component: Post },
    { path: '/tag/:tag', component: PostsByTag },
    { path: '/', component: AllPosts },
    ],
})
export default router
