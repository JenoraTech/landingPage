// ===========================
// Navbar Scroll Effect
// ===========================
const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// ===========================
// Mobile Navigation
// ===========================
const mobileToggle = document.getElementById("mobileToggle");
const navLinks = document.getElementById("navLinks");

if (mobileToggle) {
  mobileToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
    const expanded = mobileToggle.getAttribute("aria-expanded") === "true";
    mobileToggle.setAttribute("aria-expanded", !expanded);
  });
}

document.querySelectorAll(".nav-links a").forEach(link => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("active");
    if (mobileToggle) {
      mobileToggle.setAttribute("aria-expanded", "false");
    }
  });
});

// ===========================
// Scroll Reveal Animation
// ===========================
const revealObserver = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.15 }
);

document.querySelectorAll(".animate-on-scroll").forEach(el => {
  revealObserver.observe(el);
});

// ===========================
// FAQ Accordion
// ===========================
document.querySelectorAll(".faq-item").forEach(item => {
  const question = item.querySelector(".faq-question");

  question.addEventListener("click", () => {
    const isActive = item.classList.contains("active");

    document.querySelectorAll(".faq-item").forEach(i => {
      i.classList.remove("active");
      i.querySelector(".faq-question").setAttribute("aria-expanded", "false");
    });

    if (!isActive) {
      item.classList.add("active");
      question.setAttribute("aria-expanded", "true");
    }
  });
});

// ===========================
// Stat Counter Animation
// ===========================
const counters = document.querySelectorAll(".stat-number");

const counterObserver = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const counter = entry.target;
      const target = parseInt(counter.dataset.target, 10);
      let current = 0;
      const increment = Math.max(target / 120, 1);

      const update = () => {
        current += increment;
        if (current < target) {
          counter.innerText = Math.floor(current);
          requestAnimationFrame(update);
        } else {
          counter.innerText = target + "+";
        }
      };

      update();
      counterObserver.unobserve(counter);
    });
  },
  { threshold: 0.5 }
);

counters.forEach(counter => counterObserver.observe(counter));

// ===========================
// Smooth Scroll for Anchor Links
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    const targetId = this.getAttribute("href");
    if (targetId === "#" || targetId.length < 2) return;

    const target = document.querySelector(targetId);
    if (!target) return;

    e.preventDefault();
    target.scrollIntoView({ behavior: "smooth" });
  });
});

// ===========================
// Contact Form
// ===========================
const contactForm = document.getElementById("contactForm");

if (contactForm) {
  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = this.querySelector('[name="name"]').value.trim();
    const email = this.querySelector('[name="email"]').value.trim();

    if (!name || !email) {
      alert("Please fill in your name and email.");
      return;
    }

    alert("Thanks! Your message has been received. We'll be in touch shortly.");
    this.reset();
  });
}

// ===========================
// "Book a Free Demo" CTA button
// ===========================
const ctaDemoBtn = document.getElementById("ctaDemoBtn");

if (ctaDemoBtn) {
  ctaDemoBtn.addEventListener("click", e => {
    e.preventDefault();
    const form = document.getElementById("contactForm");
    if (form) {
      form.scrollIntoView({ behavior: "smooth" });
      form.querySelector('[name="name"]').focus({ preventScroll: true });
    }
  });
}

// ===========================
// Newsletter Form
// ===========================
const newsletter = document.querySelector(".newsletter-form");

if (newsletter) {
  newsletter.addEventListener("submit", function (e) {
    e.preventDefault();

    const input = this.querySelector("input");

    if (!input.value.trim()) {
      alert("Please enter your email address.");
      return;
    }

    alert("Thank you for subscribing!");
    input.value = "";
  });
}