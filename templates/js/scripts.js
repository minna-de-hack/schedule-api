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
  const title = document.getElementById("titleInput").value;
  const description = document.getElementById("descriptionInput").value;
  const startDates = document.getElementById("startDatesInput").value; // "2023-05-10"
  const startTime = document.getElementById("startTimeInput").value; // "21:10"
  const endDates = document.getElementById("endDatesInput").value; // "2023-05-10"
  const endTime = document.getElementById("endTimeInput").value; // "21:10"

  var startDatesTime = startDates.split("-").join('') +"T"+ startTime.split(":").join('') + "00"
  var endDatesTime = endDates.split("-").join('') +"T"+ endTime.split(":").join('') + "00"

  var url = window.location.origin + "/api"

  const params = {
      title: title == "" ? "無題" : title,
      description: description,
      dates: startDatesTime + "/" + endDatesTime
  }
  const urlSearchParam =  new URLSearchParams(params).toString();

  var url = url + "?" + urlSearchParam  

  var output = document.getElementById("exportTarget");  
  var tags = `<iframe id="embedded-schedule" scrolling="no" style="border:0" src="${url}"></iframe>`
  output.textContent = tags;

  var button = document.getElementById("insertbutton");
  button.innerHTML = `<button class="btn btn-outline-secondary" onclick="copyToClipboard()">Copy text</button>`;

  // insertElements
  var targetElement = document.getElementById("insertElement");

  var newDiv = document.createElement("div");
  newDiv.textContent = "新しい要素がここに表示されます";
  newDiv.setAttribute("id", "insertOldElement");

  var inner = `<a>Sample</a><div class="EmbedCode-sample-content">${tags}</div>`;
  newDiv.innerHTML = inner;
 
  var oldDiv = document.getElementById('insertOldElement');
  targetElement.replaceChild(newDiv, oldDiv);
}