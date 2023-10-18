<template>
    <div class="login-container">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
            <div class="input-group">
                <label for="username">Username:</label>
                <input type="text" id="username" v-model="username" placeholder="Enter your username" required>
            </div>
            <div class="input-group">
                <label for="password">Password:</label>
                <input type="password" id="password" v-model="password" placeholder="Enter your password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';  

export default {
    setup() {
        const router = useRouter();
        const username = ref('');
        const password = ref('');
        const errorMessage = ref('');

        const handleLogin = async () => {
            try {
                const response = await axios.post('http://localhost:8000/login/get_token', {
                    username: username.value,
                    password: password.value
                });
                if (response.data.success) {
                    router.push('/index');
                } else {
                    errorMessage.value = '账号或密码错误';
                }
            } catch (error) {
                errorMessage.value = '登录失败，请稍后再试';
            }
        };

        return {
            username,
            password,
            errorMessage,
            handleLogin
        };
    }
}
</script>

<style scoped>
.login-container {
    width: 300px;
    max-width: 90%;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}


h2 {
    text-align: center;
    margin-bottom: 20px;
}

.input-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
