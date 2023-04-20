import { accountService } from "@/service";
import router from "@/router";

export function authGuard() {
    if(accountService.isLogged()) {
        return true 
    }
    router.push('/login')
}