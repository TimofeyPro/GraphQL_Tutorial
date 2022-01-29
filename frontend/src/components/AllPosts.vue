<template>
  <div>
    <h2>Recent posts</h2>
    <PostList v-if="allPosts" :posts="allPosts" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import PostList from '@/components/PostList'

export default {
  name: 'AllPosts',
  components: {
    PostList,
  },
  data () {
    return {
        allPosts: null,
    }
  },
  async created () {
    const posts = await this.$apollo.query({
      query: gql`query {
        allPosts {
          title
          subtitle
          publishDate
          published
          metaDescription
          slug
          author {
            user {
              username
              firstName
              lastName
            }
          }
          tags {
            name
          }
        }
      }`,
    })
    this.allPosts = posts.data.allPosts
  },
}
</script>


