import axios from 'axios';

const ADDRESS = "http://localhost:3100";

export default class NoPlpBackendApi {
    static getUrl() {
        return ADDRESS;
    }

    static async newRound() {
        let {data} = await axios.put(NoPlpBackendApi.getUrl() + "/round");

        return data;
    }

    static async getRound(roundid) {
        let {data} = await axios.get(NoPlpBackendApi.getUrl() + `/round/${roundid}`);
        return data;
    }

    static async getSongsFromCategory(category) {
        let {data} = await axios.get(NoPlpBackendApi.getUrl() + `/category/${category}/songs`);

        return data;
    }

    static async getSong(artist, title, level) {
        let {data} = await axios.get(NoPlpBackendApi.getUrl() + `/song/artist/${artist}/title/${title}/level/${level}`);

        return data;
    }

    static async getAdminSong(challengeid) {
        let {data} = await axios.get(NoPlpBackendApi.getUrl() + `/admin/challenge/${challengeid}`);

        return data;
    }

    // static async downloadFromLink(link, appid) {
    //     let appCookies = AppBackendApi.getCookies();
    //     let payload = {
    //         link: link,
    //         app: appid
    //     };
    //     let {data} = await axios.post(AppBackendApi.getUrl() + "/downloadFromLink.json", payload, {headers: { 'Content-Type': 'application/json', 'DevCookie': appCookies.token, 'APIC-challenge': appCookies.urlToken }});
        
    //     return data; 
    // }

    // static async getLatestTasks() {
    //     let appCookies = AppBackendApi.getCookies();
    //     let resp = await axios({url: AppBackendApi.getUrl() + "/tasks/latest.json", method: "GET", headers: { 'Content-Type': 'application/json', 'DevCookie': appCookies.token, 'APIC-challenge': appCookies.urlToken }});
    //     return resp;
    // }

    // static async status() {
    //     let appCookies = AppBackendApi.getCookies();
    //     let {data} = await axios.get(AppBackendApi.getUrl() + "/system/status.json", {headers: { 'Content-Type': 'application/json', 'DevCookie': appCookies.token, 'APIC-challenge': appCookies.urlToken }});

    //     return data.status;
    // }

    // static async getLastSync() {
    //     let appCookies = AppBackendApi.getCookies();
    //     let {data} = await axios.get(AppBackendApi.getUrl() + "/system/last_sync.json", {headers: { 'Content-Type': 'application/json', 'DevCookie': appCookies.token, 'APIC-challenge': appCookies.urlToken }});

    //     return data.last_sync;
    // }

    // static async getLastTrySync() {
    //     let appCookies = AppBackendApi.getCookies();
    //     let {data} = await axios.get(AppBackendApi.getUrl() + "/system/last_try_sync.json", {headers: { 'Content-Type': 'application/json', 'DevCookie': appCookies.token, 'APIC-challenge': appCookies.urlToken }});

    //     return data.last_try_sync;
    // }
}