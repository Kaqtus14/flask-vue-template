import axios from 'axios';

export const http = axios.create({
    baseURL: window.location.href.includes("127.0.0.1") ? "http://127.0.0.1:5000" : "/",
    headers: {
        "Content-Type": "application/json",
    },
    withCredentials: true,
})
