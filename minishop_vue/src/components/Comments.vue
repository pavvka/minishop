<template>
    <div class="column is-9">
        <h3 class="is-size-6 mb-6">KEK: {{ comment.user }}</h3>

    </div>
</template>

<script>
export default {
    name: 'Comments',
    props: {
        comment: Object
    },
    methods: {

    }
}
</script>