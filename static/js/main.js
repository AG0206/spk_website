/* ═══════════════════════════════════════════════
   SPK Organisation — Main JavaScript
   Features:
   · Sticky navbar + active section highlight
   · Smooth scroll for anchor links
   · Mobile nav toggle
   · Counter animation (hero stats)
   · Gallery filter + Lightbox
   · Contact form UX
   · AOS init
═══════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ─────────────────────────────────────────────
     1. AOS (Animate On Scroll) Init
  ───────────────────────────────────────────── */
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 700,
      easing: 'ease-out-cubic',
      once: true,
      offset: 80,
    });
  }

  /* ─────────────────────────────────────────────
     2. Navbar: scroll class + active link highlight
  ───────────────────────────────────────────── */
  const nav       = document.getElementById('mainNav');
  const navLinks  = document.querySelectorAll('.nav-links .nav-link:not(.nav-cta)');
  const sections  = document.querySelectorAll('section[id]');

  function onScroll () {
    // Scrolled shadow
    if (window.scrollY > 40) nav.classList.add('scrolled');
    else                      nav.classList.remove('scrolled');

    // Active link highlight
    let currentId = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) currentId = sec.id;
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ─────────────────────────────────────────────
     3. Smooth scroll for ALL anchor links
  ───────────────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (!target) return;
      e.preventDefault();

      const navH = nav ? nav.offsetHeight : 76;
      const top  = target.getBoundingClientRect().top + window.scrollY - navH;

      window.scrollTo({ top, behavior: 'smooth' });

      // Close mobile menu if open
      closeMobileNav();
    });
  });

  /* ─────────────────────────────────────────────
     4. Mobile Nav Toggle
  ───────────────────────────────────────────── */
  const navToggler = document.getElementById('navToggler');
  const navLinksEl = document.getElementById('navLinks');

  function closeMobileNav () {
    navToggler?.classList.remove('open');
    navLinksEl?.classList.remove('open');
    document.body.style.overflow = '';
  }

  navToggler?.addEventListener('click', () => {
    const open = navLinksEl.classList.toggle('open');
    navToggler.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });

  // Close on outside click
  document.addEventListener('click', e => {
    if (!nav.contains(e.target)) closeMobileNav();
  });

  /* ─────────────────────────────────────────────
     5. Hero Counter Animation
  ───────────────────────────────────────────── */
  const counters = document.querySelectorAll('.hstat-num[data-count]');
  let countersStarted = false;

  function startCounters () {
    if (countersStarted) return;
    const heroStats = document.querySelector('.hero-stats');
    if (!heroStats) return;
    const rect = heroStats.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
      countersStarted = true;
      counters.forEach(el => animateCount(el));
    }
  }

  function animateCount (el) {
    const target = parseInt(el.dataset.count, 10);
    const duration = 1800;
    const start = performance.now();

    function step (now) {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out-expo
      const eased    = 1 - Math.pow(2, -10 * progress);
      el.textContent = Math.floor(eased * target).toLocaleString('en-IN');
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target.toLocaleString('en-IN');
    }
    requestAnimationFrame(step);
  }

  window.addEventListener('scroll', startCounters, { passive: true });
  startCounters(); // attempt immediately (hero visible on load)

  /* ─────────────────────────────────────────────
     6. Gallery Filter
  ───────────────────────────────────────────── */
  const filterBtns  = document.querySelectorAll('.gf-btn');
  const galleryItems = document.querySelectorAll('.g-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;
      galleryItems.forEach(item => {
        if (filter === 'all' || item.dataset.cat === filter) {
          item.classList.remove('hidden');
          item.style.animation = 'fadeIn .4s ease both';
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });

  /* ─────────────────────────────────────────────
     7. Lightbox
  ───────────────────────────────────────────── */
  const overlay    = document.getElementById('lightboxOverlay');
  const lbImg      = document.getElementById('lightboxImg');
  const lbClose    = document.getElementById('lightboxClose');
  const lbPrev     = document.getElementById('lightboxPrev');
  const lbNext     = document.getElementById('lightboxNext');

  let lbImages   = [];
  let lbCurrent  = 0;

  function buildImageList () {
    lbImages = [];
    document.querySelectorAll('.g-item:not(.hidden) img').forEach(img => {
      lbImages.push({ src: img.src, alt: img.alt });
    });
  }

  function openLightbox (idx) {
    buildImageList();
    lbCurrent = idx;
    showLightboxImage();
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox () {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  function showLightboxImage () {
    if (!lbImages.length) return;
    const { src, alt } = lbImages[lbCurrent];
    lbImg.src = src;
    lbImg.alt = alt;
  }

  // Open on g-item click
  document.querySelectorAll('.g-item').forEach((item, i) => {
    item.addEventListener('click', () => openLightbox(i));
  });

  lbClose?.addEventListener('click', closeLightbox);
  overlay?.addEventListener('click', e => { if (e.target === overlay) closeLightbox(); });

  lbPrev?.addEventListener('click', () => {
    lbCurrent = (lbCurrent - 1 + lbImages.length) % lbImages.length;
    showLightboxImage();
  });
  lbNext?.addEventListener('click', () => {
    lbCurrent = (lbCurrent + 1) % lbImages.length;
    showLightboxImage();
  });

  // Keyboard nav
  document.addEventListener('keydown', e => {
    if (!overlay.classList.contains('active')) return;
    if (e.key === 'Escape')       closeLightbox();
    if (e.key === 'ArrowLeft')  { lbCurrent = (lbCurrent - 1 + lbImages.length) % lbImages.length; showLightboxImage(); }
    if (e.key === 'ArrowRight') { lbCurrent = (lbCurrent + 1) % lbImages.length; showLightboxImage(); }
  });

  // Touch swipe support in lightbox
  let touchStartX = 0;
  overlay?.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].clientX; }, { passive: true });
  overlay?.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) { lbCurrent = (lbCurrent + 1) % lbImages.length; }
      else          { lbCurrent = (lbCurrent - 1 + lbImages.length) % lbImages.length; }
      showLightboxImage();
    }
  }, { passive: true });

  /* ─────────────────────────────────────────────
     8. Contact Form UX
  ───────────────────────────────────────────── */
  const contactForm = document.getElementById('contactForm');
  const submitBtn   = document.getElementById('submitBtn');
  const formSuccess = document.getElementById('formSuccess');

  contactForm?.addEventListener('submit', e => {
    // If Django backend handles it, remove preventDefault and let it submit
    // For now, provide loading feedback while preserving Django form POST
    submitBtn.innerHTML = '<span class="spinner"></span> Sending…';
    submitBtn.style.opacity = '.7';
    submitBtn.disabled = true;
    // Django will process; if no backend, show success after timeout (demo)
    // Comment out the setTimeout block if Django handles the redirect/response
    setTimeout(() => {
      submitBtn.innerHTML = '<i class="bi bi-send-fill"></i> Send Message';
      submitBtn.style.opacity = '1';
      submitBtn.disabled = false;
    }, 8000);
  });

  /* ─────────────────────────────────────────────
     9. WhatsApp float — shrink label on scroll
  ───────────────────────────────────────────── */
  const waFloat = document.querySelector('.whatsapp-float');
  window.addEventListener('scroll', () => {
    if (!waFloat) return;
    // Already handled by CSS media query; extra shrink on scroll
    if (window.scrollY > 200) waFloat.style.borderRadius = '50px';
    else waFloat.style.borderRadius = '100px';
  }, { passive: true });

}); // end DOMContentLoaded
