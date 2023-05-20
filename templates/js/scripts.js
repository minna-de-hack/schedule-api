function copyToClipboard() {
    var exportTarget = document.getElementById("exportTarget").innerText;
    navigator.clipboard.writeText(exportTarget)
    .then(() => {
      console.log("テキストがクリップボードにコピーされました");
      alert("クリップボードにコピーされました");
    })
    .catch((error) => {
      console.error("コピーに失敗しました", error);
      alert("コピーに失敗しました : " + error);
    });
}

function createTags(){
    var title = document.getElementById("titleInput").value;
    var description = document.getElementById("descriptionInput").value;
    var start = document.getElementById("startDatesInput").value;
    var end = document.getElementById("endDatesInput").value;

    console.log("入力された情報:", title);    

    var output = document.getElementById("exportTarget");
    var tags = ""

    output.textContent = tags;
}
// https://github.com/minna-de-hack/testHTML/blob/main/src/views/WatchView.vue
// 
// import Event from '../assets/event.json'
// import { useRouter } from 'vue-router'
// import { ref, onMounted } from 'vue'

// const router = useRouter()

// const eventData = Event.event
// const title = ref()
// const description = ref()
// const date_start = ref()
// const date_end = ref()
// const URL = ref()

// onMounted(() => {
//     const num = Number( location.pathname.split("/").slice(-2)[1] )
//     title.value = eventData[num]["title"]
//     description.value = eventData[num]["description"]
//     date_start.value = ChangeDate(eventData[num]["date_start"])
//     date_end.value = ChangeDate(eventData[num]["date_end"])

//     createURL(title.value, description.value, date_start.value, date_end.value)
// })

// const ChangeDate = (dateString) => {
//     const year = parseInt(dateString.substr(0, 4));
//     const month = parseInt(dateString.substr(4, 2)) - 1;
//     const day = parseInt(dateString.substr(6, 2));
//     const hours = parseInt(dateString.substr(9, 2));
//     const minutes = parseInt(dateString.substr(11, 2));
//     const seconds = parseInt(dateString.substr(13, 2));

//     const date = new Date(year, month, day, hours, minutes, seconds);
//     const formattedDate = `${date.getFullYear()}/${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}`;
//     return formattedDate
// }

// const createURL = (title, description, date_start, date_end) => {
//     URL.value = "http://127.0.0.1:8000/api?title=" + title + "&description=" + description + "&dates=" + date_start + "/" + date_end
// }

// const HOME = () => {
//     router.push('/')
// }

// const Registration = () => {
//     alert("参加登録をしました")
// }
