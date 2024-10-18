    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const userName = "{{ user.username }}";
            const message = `Hi ${userName}, welcome to your profile info page!`;
            const element = document.getElementById('welcome-message');
            let index = 0;

            function typeLetter() {
                if (index < message.length) {
                    element.textContent += message.charAt(index);
                    index++;
                    setTimeout(typeLetter, 100); // Adjust typing speed (100ms per letter)
                }
            }

            typeLetter();
        });
    </script>