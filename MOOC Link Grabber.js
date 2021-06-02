var completed = document.querySelectorAll(".section-item");
var download;
var i, j = 0;
let rows = [["Unit name", "Chapter Name", 'URL']];

let timerId = setInterval(()=>{
    if (j !== completed.length - 1) {
        i = completed[j];
        download = document.querySelector(".download");
        let unitName = i.parentElement.parentElement.firstElementChild.innerText;

//         let chapterName = i.getElementsByClassName('lecture-name')[0].textContent.trim().split("  ")[0].trim();
        let chapterName = i.getElementsByClassName('lecture-name')[0].innerText;
           
          console.info(`download: ${download}, chapterName: ${chapterName}, unitName: ${unitName}`)
        if (!download) {
            //rows.push([chapterName, "Twitter or some other feedback form"]);
//             break;
        j++;
        i = completed[j];
        i.firstElementChild.click();
        return;
        }

        rows.push([unitName, chapterName, (!download) ? '' : download.href]);

        j++;
        i = completed[j];
        i.firstElementChild.click();
        return;
        
    }

    let csvContent = "data:text/csv;charset=utf-8," + rows.map(e=>e.join(",")).join("\n");
    let encodedUri = encodeURI(csvContent);
    let title = document.querySelector('.course-sidebar > h2').innerText;

    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", title + '.csv');
    // document.body.appendChild(link); required for FireFox
    link.click();
    clearInterval(timerId);
}
, 3500);