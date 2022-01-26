<template>
    <div class="column is-5">
        <p>Feel free to edit any of your details below so your account is totally up to date.</p>
            <div class="field">
            <label class="label">Username</label>
            <div class="control has-icons-left has-icons-right">
                <input class="input is-success" type="text" placeholder="username" v-model="username">
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
                <input class="input is-danger" type="email" placeholder="Email input" v-model="email">
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
                    <input class="input is-success" type="text" placeholder="Your city" v-model="city">
                </div>
            </div>

            <div class="field">
                <label class="label">Date of birth</label>
                <div class="control">
                    <input class="input is-success" type="date" placeholder="Date of birth" v-model="date_of_birth">
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
                <button class="button is-success" @click="submitForm">Save changes</button>
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
        data() {
        return {
            username: this.userdata.username,
            email: this.userdata.email,
            city: this.userdata.city,
            date_of_birth: this.userdata.date_of_birth,

        }
    },
    methods: {
        async submitForm(){
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username field is missing!')
            }
            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }
            if (this.city === '') {
                this.errors.push('The city field is missing!')
            }
            if (this.date_of_birth === '') {
                this.errors.push('The date of birth field is missing!')
            }

            const data = {
                'username': this.username,
                'email': this.email,
                'city': this.city,
                'date_of_birth': this.date_of_birth,
            }
            if (!this.errors.length) {
                await axios
                    .post('/api/v1/users/' + this.userdata.id, data)
                    .then(response => {
                        console.log(response);
                    })
                    .catch(error => {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(error)
                    })
                    this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>