const searchForm = document.getElementById("searchForm");
const pageLinks = document.getElementsByClassName("page-link");

if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();

      page = this.dataset.page;

      searchForm.innerHTML += `<input value="${page}" name="page" type="hidden"/>`;

      searchForm.submit();
    });
  }
}
