/* Genesis rebuild — interactions */
(function () {
  "use strict";

  /* ---- Animated hero: swapping words (vanilla, no libs) ----
     JS toggles .is-active / .is-prev on each .word; CSS transitions
     handle the slide+fade. Exactly one word visible at a time. */
  document.querySelectorAll("[data-swap]").forEach(function (host) {
    var spans = host.querySelectorAll(".word");
    if (!spans.length) return;
    var i = 0;
    spans[0].classList.add("is-active");
    setInterval(function () {
      var prev = spans[i];
      i = (i + 1) % spans.length;
      var next = spans[i];
      prev.classList.remove("is-active");
      prev.classList.add("is-prev");
      // clear is-prev on the one that just left so it can re-enter from bottom later
      spans.forEach(function (s) {
        if (s !== next && s !== prev) s.classList.remove("is-prev");
      });
      next.classList.remove("is-prev");
      // force reflow so the transition runs from the bottom
      void next.offsetWidth;
      next.classList.add("is-active");
    }, 2000);
  });

  /* ---- Mobile drawer ---- */
  var burger = document.getElementById("burgerBtn");
  var drawer = document.getElementById("mobileNav");
  if (burger && drawer) {
    function setOpen(open) {
      drawer.classList.toggle("open", open);
      burger.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    }
    burger.addEventListener("click", function () { setOpen(true); });
    drawer.querySelectorAll("[data-mnav-close]").forEach(function (el) {
      el.addEventListener("click", function () { setOpen(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
  }

  /* ---- Scroll reveal ---- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Product filter (category pages) ---- */
  document.querySelectorAll("[data-filter-group]").forEach(function (group) {
    var buttons = group.querySelectorAll(".chip[data-filter]");
    var items = document.querySelectorAll("[data-cat-item]");
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.classList.remove("chip--active"); });
        b.classList.add("chip--active");
        var f = b.getAttribute("data-filter");
        items.forEach(function (it) {
          var show = f === "all" || it.getAttribute("data-cat") === f;
          it.style.display = show ? "" : "none";
        });
      });
    });
  });

  /* ---- Title search filter (category pages) ---- */
  var sInput = document.querySelector("[data-search-input]");
  if (sInput) {
    var items = document.querySelectorAll("[data-cat-item]");
    sInput.addEventListener("input", function () {
      var q = sInput.value.trim().toLowerCase();
      items.forEach(function (it) {
        var t = (it.getAttribute("data-title") || "").toLowerCase();
        it.style.display = (!q || t.indexOf(q) !== -1) ? "" : "none";
      });
    });
  }

  /* ---- Tilt banner toward cursor (3D card effect) ---- */
  document.querySelectorAll(".banner-bleed").forEach(function (card) {
    card.addEventListener("mousemove", function (e) {
      var r = card.getBoundingClientRect();
      var x = e.clientX - r.left, y = e.clientY - r.top;
      var rx = ((y - r.height / 2) / (r.height / 2)) * -8;
      var ry = ((x - r.width / 2) / (r.width / 2)) * 8;
      card.style.transform = "perspective(1000px) rotateX(" + rx + "deg) rotateY(" + ry + "deg) scale3d(1.02,1.02,1.02)";
      card.style.transition = "transform 0.1s ease-out";
    });
    card.addEventListener("mouseleave", function () {
      card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)";
      card.style.transition = "transform 0.4s ease-in-out";
    });
  });

  /* ---- ⌘K / Ctrl+K focus search ---- */
  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      var s = document.querySelector("[data-search-input]");
      if (s) s.focus();
    }
  });
})();
