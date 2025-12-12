// Project Data
const projects = [
    {
        title: "Cycling Mobility",
        description: "In this article for Nexos magazine I get insights from EcoBici, the largest cycling mobility service in CDMX, in three main storylines: Users profile, connectivity with other public transport services, and surrounding security.",
        tags: ["Data Analytisis", "Python", "Matplotlib", "Pandas"],
        link: "https://datos.nexos.com.mx/un-recorrido-por-el-sistema-de-bicicletas-publicas-de-la-ciudad-de-mexico-ecobici/",
        github: "https://github.com/CAMM961001/movilidad_bicicletas",
        image: "./assets/project-banners/cycling_movility.png"
    },
    {
        title: "A Bayesian Approach",
        description: "Statistics are really cool! I didn't know that until I started my Master's program. In this brief blog I try to show the differences between a frequentist approach and a bayesian one, with an applied example.",
        tags: ["Statistics", "Quarto", "Bayesian Analysis"],
        link: "https://camm961001.quarto.pub/bayes-first-steps/chapters/english.html",
        github: "https://github.com/CAMM961001/bayes-first-steps",
        image: "./assets/project-banners/bayesian_approach.png"
    }
];

// Timeline Data
// Search icons: https://feathericons.com/
const timelineData = [
    { year: "Feb 2024", title: "The Lead Data Scientist", description: "Certified GCP ML Engineer and Cloud Developer.<br>Built customer segmentation, forecasting, & marketing mix models.<br>Developed recommendation systems, and API integrations to SQL warehouse (medallion architecture).", icon: "award" },
    { year: "Sep 2023", title: "The Master", description: "Graduated from ITAM Master of Science in Data Science", icon: "book-open" },
    { year: "Aug 2022", title: "The Data Scientist", description: "Started GCP journey.<br>Built anomaly detection systems for retail inventory management.", icon: "briefcase" },
    { year: "Apr 2021", title: "The Data Analyst", description: "First job as Data Analyst at local financial services company.<br>Implemented data pipelines for back office and compliance.<br>Developed data visualizations with Python.", icon: "briefcase" },
    { year: "2020", title: "A New Beginning", description: "Learned Python for data analysis and visualization.<br>Started data analyst journey with online courses.", icon: "refresh-ccw" },
    { year: "2019", title: "The Engineer", description: "Graduated from UNAM School of Engineering.", icon: "book-open" },
    { year: "2015", title: "UNAM Motorsports", description: "Enrolled to the Formula SAE, an international competition for undergraduate students.", icon: "book-open" },
];

// Gallery Data
const galleryImages = [
    { src: "./assets/galery/liverpool.jpg", caption: "Liverpool Purchasing Analytics Team" },
    { src: "./assets/galery/itam.jpg", caption: "ITAM CDAS Projects Presentations" },
    { src: "./assets/galery/bilstein.jpg", caption: "Bilstein MPP Process Team" },
    { src: "./assets/galery/um4.jpg", caption: "UM10 Kickoff Photo Shooting 2019" },
    { src: "./assets/galery/um3.jpg", caption: "Formula SAE Lincoln 2018" },
    { src: "./assets/galery/um2.jpg", caption: "Formula ATA Italy 2017" },
    { src: "./assets/galery/um1.jpg", caption: "UM46-7 Vehicle Rollout Event 2016" },
];

// Populate Projects
const projectContainer = document.getElementById('project-container');

function renderProjects() {
    projects.forEach(project => {
        const card = document.createElement('div');
        card.className = 'project-card';
        
        const tagsHtml = project.tags.map(tag => `<span class="skill-tag" style="font-size: 0.8rem; margin-right: 5px;">${tag}</span>`).join('');
        
        card.innerHTML = `
            <div class="project-image-container">
                <img src="${project.image}" alt="${project.title}" class="project-image">
            </div>
            <div class="project-content">
                <h3 class="project-title">${project.title}</h3>
                <p class="project-desc">${project.description}</p>
                <div style="margin-bottom: 1rem;">
                    ${tagsHtml}
                </div>
                <div class="project-links">
                    <a href="${project.github}" target="_blank" class="btn" style="padding: 0.4rem 1rem; font-size: 0.8rem;">GitHub</a>
                    <a href="${project.link}" target="_blank" style="text-decoration: underline;">View Live</a>
                </div>
            </div>
        `;
        
        projectContainer.appendChild(card);
    });
}

// Render Timeline
function renderTimeline() {
    const timelineWrapper = document.getElementById('timeline-wrapper');
    if (!timelineWrapper) return;

    let html = '<div class="timeline">';
    timelineData.forEach((item, index) => {
        html += `
            <div class="timeline-item">
                <div class="timeline-icon">
                    <i data-feather="${item.icon}"></i>
                </div>
                <div class="timeline-content">
                    <span class="timeline-year">${item.year}</span>
                    <h3 class="timeline-title">${item.title}</h3>
                    <p class="timeline-desc">${item.description}</p>
                </div>
            </div>
        `;
    });
    html += '</div>';
    timelineWrapper.innerHTML = html;
    if (typeof feather !== 'undefined') {
        feather.replace();
    }
}

// Gallery Logic
let currentSlide = 0;
const slideIntervalTime = 4000; // 3 seconds
let slideInterval;

function initGallery() {
    const wrapper = document.getElementById('gallery-wrapper');
    const captionEl = document.getElementById('gallery-caption');
    const indicatorsEl = document.getElementById('gallery-indicators');
    
    if (!wrapper || galleryImages.length === 0) return;

    // Render Images
    galleryImages.forEach((img, index) => {
        const slide = document.createElement('div');
        slide.className = `gallery-slide ${index === 0 ? 'active' : ''}`;
        slide.innerHTML = `<img src="${img.src}" alt="${img.caption}">`;
        wrapper.appendChild(slide);

        // Render Indicator
        const indicator = document.createElement('div');
        indicator.className = `indicator ${index === 0 ? 'active' : ''}`;
        indicator.addEventListener('click', () => {
            goToSlide(index);
            resetInterval();
        });
        indicatorsEl.appendChild(indicator);
    });

    // Set initial caption
    captionEl.textContent = galleryImages[0].caption;

    // Start Auto Play
    startInterval();
}

function goToSlide(index) {
    const slides = document.querySelectorAll('.gallery-slide');
    const indicators = document.querySelectorAll('.indicator');
    const captionEl = document.getElementById('gallery-caption');

    if (slides.length === 0) return;

    // Remove active class
    slides[currentSlide].classList.remove('active');
    indicators[currentSlide].classList.remove('active');

    // Update index
    currentSlide = index;
    if (currentSlide >= slides.length) currentSlide = 0;
    if (currentSlide < 0) currentSlide = slides.length - 1;

    // Add active class
    slides[currentSlide].classList.add('active');
    indicators[currentSlide].classList.add('active');
    
    // Update Caption
    captionEl.textContent = galleryImages[currentSlide].caption;
}

function nextSlide() {
    goToSlide(currentSlide + 1);
}

function startInterval() {
    slideInterval = setInterval(nextSlide, slideIntervalTime);
}

function resetInterval() {
    clearInterval(slideInterval);
    startInterval();
}

// Mobile Menu Logic
const mobileBtn = document.getElementById('mobile-menu-btn');
const navMenu = document.getElementById('nav-menu');

if (mobileBtn) {
    mobileBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        // Optional: Toggle icon between menu and x
    });
}

// Fade In Animation on Scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    renderProjects();
    renderTimeline();
    initGallery();
    
    // Add animation classes
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(section);
    });
});
