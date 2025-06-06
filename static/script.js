function drawWheel(prizes) {
    const canvas = document.getElementById('wheel');
    const ctx = canvas.getContext('2d');
    const arc = Math.PI * 2 / prizes.length;

    for (let i = 0; i < prizes.length; i++) {
        ctx.beginPath();
        ctx.fillStyle = i % 2 === 0 ? '#f8b500' : '#fceabb';
        ctx.moveTo(250, 250);
        ctx.arc(250, 250, 240, arc * i, arc * (i + 1));
        ctx.closePath();
        ctx.fill();
        ctx.save();
        ctx.translate(250, 250);
        ctx.rotate(arc * i + arc / 2);
        ctx.fillStyle = '#000';
        ctx.textAlign = 'center';
        ctx.fillText(prizes[i], 160, 5);
        ctx.restore();
    }
}

function spinWheel(index) {
    const wheel = document.getElementById('wheel');
    const degPerPrize = 360 / prizes.length;
    const rotation = 360 * 3 + (index * degPerPrize) + degPerPrize / 2;
    wheel.style.transform = `rotate(-${rotation}deg)`;
}

window.onload = function() {
    drawWheel(prizes);
    document.getElementById('spin').onclick = async function() {
        const res = await fetch('/spin');
        const data = await res.json();
        spinWheel(data.index);
        document.getElementById('result').innerText = `恭喜獲得 ${data.prize} 元！`;
    };
};
