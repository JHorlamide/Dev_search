// const hljs = require('highlight.js');

// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  let alertWrapper = document.querySelector('.alert');
	let alertClose = document.querySelector('.alert__close');

	if (alertWrapper) {
		alertClose.addEventListener('click', (e) => {
			alertWrapper.style.display = 'none';
		});
	}

	// hljs.highlightAll();
});

// document.addEventListener('DOMContentLoaded', (event) => {
// 	document.querySelectorAll('pre code').forEach((el) => {
// 		hljs.highlightElement(el);
// 	});
// });

// let alertWrapper = document.querySelector('.alert');
// let alertClose = document.querySelector('.alert__close');

// if (alertWrapper) {
// 	alertClose.addEventListener('click', (e) => {
// 		alertWrapper.style.display = 'none';
// 	});
// }
