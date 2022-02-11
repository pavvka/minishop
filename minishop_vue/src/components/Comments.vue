<template>
    <div class="box mb-4">
        <h3 class="is-size-6">{{ comment.user }}: </h3>
        <span class="is-size-7 grey">{{ comment.created_date }}</span>
        <p class="">{{ comment.text }}</p>

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