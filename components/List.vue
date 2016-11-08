<template lang="html">
    <md-list class="custom-list md-triple-line">
      <md-list-item v-for="vote in votes">
        <md-avatar>
          <img src="https://placeimg.com/40/40/people/1" alt="People">
        </md-avatar>

        <div class="md-list-text-container">
          <span>{{ vote.author_name }}</span>
          <span>{{ vote.content }}</span>
          <p>
              <span v-for='voter in vote.voters'>{{ voter }} </span>
          </p>
        </div>

        <md-button class="md-icon-button md-list-action">
          <md-icon class="md-primary">star</md-icon>
        </md-button>

        <md-divider class="md-inset"></md-divider>
      </md-list-item>
  </md-list>
</template>

<script>
export default {
    props: [
        'votes'
    ]
}
</script>

<style lang="css">
</style>
