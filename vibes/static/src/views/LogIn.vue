<template>
    <div id="log-in" class="djoser">
        <div class="auth">
            <h1 class="auth__title">Log In</h1>
            <form class="auth__form">
                <div class="auth__input-container">
                    <div class="auth__label-container">
                        <label class="auth__label">Email address</label>
                        <a href="" class="auth__label-link">Forgot?</a>
                    </div>
                    <input v-model="email" class="auth__input" type="text" placeholder="you@domain.com" spellcheck="false" autofocus>
                </div>
                <div class="auth__input-container">
                    <div class="auth__label-container">
                        <label class="auth__label">Password</label>
                        <a href="" class="auth__label-link">Forgot?</a>
                    </div>
                    <input v-model="password" class="auth__input" type="password" placeholder="Super, secret">
                </div>
                <button v-on:click.prevent="logIn" class="auth__button--primary">Log In</button>
            </form>
            <p class="auth__help">New here? <router-link :to="{ name: 'signup' }">Create an account</router-link></p>
        </div>
    </div>
</template>

<script>
import router from '../router'
import store from '../store'
import axios from 'axios'

export default {
    name: 'log-in',

    data: function () {
        return {
            email: null,
            password: null
        }
    },

    methods: {
        logIn: function () {
            const data = {
                email: this.email,
                password: this.password
            }
            store.dispatch('POST_TOKEN', data).then(() => {
                var instance = axios.create({
                    baseURL: '/api/v1/',
                    headers: {'Authorization': `JWT ${store.state.token}`}
                })
                instance.get('users/')
                .then(function (response) {
                    console.log(response.data)
                })
                .catch(function (error) {
                    console.log(error)
                })
            })
        }
    }
}
</script>
