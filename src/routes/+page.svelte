<script>
  import './styles.css';
  import { isModalOpen } from '../stores/modalStore.js';
  import Cover from './Cover.svelte';
  import Modal from './Modal.svelte';

  import cover1 from '../lib/images/afterburner.jpg';
  import cover2 from '../lib/images/artifical-selection.jpg';
  import cover3 from '../lib/images/dbm.jpg';
  import cover4 from '../lib/images/dgd.jpg';
  import cover5 from '../lib/images/grat.jpg';
  import cover6 from '../lib/images/happiness.jpg';
  import cover7 from '../lib/images/jackpot.jpg';
  import cover8 from '../lib/images/mothership.jpg';
  import cover9 from '../lib/images/royal-ocean.jpg';
  import cover10 from '../lib/images/speech.jpg';
  import cover11 from '../lib/images/tree-city-sessions.jpg';
  import cover12 from '../lib/images/tree-city-sessions-2.jpg';

  const albums = [
    {
      coverUrl: cover1,
      title: '',
    },
    {
      coverUrl: cover2,
      title: '',
    },
    {
      coverUrl: cover3,
      title: '',
    },
    {
      coverUrl: cover4,
      title: '',
    },
    {
      coverUrl: cover5,
      title: '',
    },
    {
      coverUrl: cover6,
      title: '',
    },
    {
      coverUrl: cover7,
      title: '',
    },
    {
      coverUrl: cover8,
      title: '',
    },
    {
      coverUrl: cover9,
      title: '',
    },
    {
      coverUrl: cover10,
      title: '',
    },
    {
      coverUrl: cover11,
      title: '',
    },
    {
      coverUrl: cover12,
      title: '',
    },
  ];
</script>

<section>
  <div class="spread">
    {#each albums as album}
      <Cover albumCoverUrl={album.coverUrl} albumTitle={album.title} />
    {/each}
  </div>

  {#if $isModalOpen}
    <Modal />
  {/if}
</section>

<style>
  section {
    color: #fff4e0;
  }

  .spread {
    max-width: 70%;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
  }
</style>
