function loadJSON() {
    let req = new XMLHttpRequest();

    req.onreadystatechange = () => {
        if (req.readyState == XMLHttpRequest.DONE) {
            console.log(req.responseText);
            jsonData = JSON.parse(req.responseText);
            jsonRecord = jsonData.record;
            document.getElementById("acft").innerText = jsonRecord.rateDaily;
            document.getElementById("curLevel").innerText = jsonRecord.percentFull;
            document.getElementById("prob1").innerText = jsonRecord.prob1;
            document.getElementById("prob2").innerText = jsonRecord.prob2;
            document.getElementById("prob3").innerText = jsonRecord.prob3;
            document.getElementById("prob4").innerText = jsonRecord.prob4;
            document.getElementById("prob5").innerText = jsonRecord.prob5;
            document.getElementById("prob6").innerText = jsonRecord.prob6;
            document.getElementById("curDate").innerText = jsonRecord.timeUpdated;
        }
    };
    req.open("GET", "https://api.jsonbin.io/v3/b/629b57ca05f31f68b3b5f9e5/latest", true);
    req.setRequestHeader("X-Master-Key", "$2b$10$dxd6lb8WQls6.4sMnC7Sv.Q2EX/oqgphwuPh2AE3MZyMz9vat7Ag6");
    req.send();
}
document.onload = loadJSON();
//document.getElementById("btn").addEventListener("click", loadJSON);