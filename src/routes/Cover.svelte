<script>
  export let albumCoverUrl;
  export let albumTitle;

  import { isModalOpen } from '../stores/modalStore.js';
</script>

<figure on:click={() => ($isModalOpen = true)}>
  <img src={albumCoverUrl} alt={albumTitle} width="150" />
</figure>

<style>
  figure,
  img {
    color: green;
    margin: 0;
    width: 100%;
    cursor: pointer;
  }
</style>
