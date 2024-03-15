const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });

}); 

const hiddenElements = document.querySelectorAll('.hidden');


// Placeholder script to toggle sidebar. Requires more detailed functionality.
document.querySelector('.sidebar').addEventListener('click', function () {
    this.classList.toggle('show');
});
document.getElementById('sidebarToggle').addEventListener('click', function () {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('show');
});;