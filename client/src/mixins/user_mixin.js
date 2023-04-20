import { accountService } from "@/service"

export default {
    data() {
        return {
            user: {},
        }
    },
    mounted() {
        if(accountService.isLogged()) {
            this.$axios.get(`${this.$api}/user/current`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: "Bearer " + accountService.getToken()
                }
            }).then(response => {
                console.log(response.data)
                this.user = response.data
            }).catch(err => {
                console.log(err)
            })
        }
    }
}