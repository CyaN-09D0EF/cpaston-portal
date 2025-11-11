// 아주 최소: 줄바꿈-><p> 정도만. (필요 시 marked 등 프론트 라이브러리로 대체)
document.querySelectorAll(".md").forEach(el=>{
  const raw = el.getAttribute("data-markdown") || "";
  const html = raw
    .split(/\n{2,}/).map(p=>`<p>${p.replace(/\n/g,"<br>")}</p>`).join("");
  el.innerHTML = html;
});

// 예: API로 섹션 수정 (PUT)
/*
fetch('/api/sections/overview', {
  method:'PUT',
  headers:{'Content-Type':'application/json'},
  body: JSON.stringify({ markdown: '새 내용' })
}).then(r=>r.json()).then(console.log)
*/
