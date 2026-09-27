  function getCookie(name) {
        let match = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
        return match ? match[2] : null;
    }

    window.onload = function() {
        if (!getCookie("role")) {
            document.cookie = "role=guest; path=/";
        }

        let role = getCookie("role");

        document.getElementById("nav-role").textContent = role;

        if (role === "admin") {
            document.getElementById("denied").style.display = "none";
            document.getElementById("flag-revealed").style.display = "block";
        } else {
            document.getElementById("role-label").textContent = "ROLE: " + role.toUpperCase();
        }
    };
