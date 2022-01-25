<template>
    <div class="column is-5">
        <p>Feel free to edit any of your details below so your account is totally up to date.</p>
            <div class="field">
            <label class="label">Username</label>
            <div class="control has-icons-left has-icons-right">
                <input class="input is-success" type="text" placeholder="username" :value="this.userdata.username">
                <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fas fa-check"></i>
                </span>
            </div>
            <p class="help is-success">This username is available</p>
            </div>

            <div class="field">
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
                <input class="input is-danger" type="email" placeholder="Email input" :value="this.userdata.email">
                <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
                </span>
            </div>
            <p class="help is-danger">This email is invalid</p>
            </div>

            <div class="field">
                <label class="label">City</label>
                <div class="control">
                    <input class="input is-success" type="text" placeholder="Your city" :value="this.userdata.city">
                </div>
            </div>

            <div class="field">
                <label class="label">Date of birth</label>
                <div class="control">
                    <input class="input is-success" type="date" placeholder="Date of birth" :value="this.userdata.date_of_birth">
                </div>
            </div>

            <div class="field">
            <div class="control">
                <label class="checkbox">
                <input type="checkbox">
                I agree to the <a href="#">terms and conditions</a>
                </label>
            </div>
            </div>

            <div class="field is-grouped">
            <div class="control">
                <button class="button is-success">Save changes</button>
            </div>
            <div class="control">
                <button class="button is-success is-light">Cancel</button>
            </div>
            </div>
    </div>
</template>

<script>
export default {
    name: 'UserDetails',
    props: {
        userdata: Object
    },
}
</script>