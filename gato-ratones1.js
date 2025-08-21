// Juego del Gato y el Ratón - Consola (Node.js)
// Versión simplificada: imprime distancias y energía al cazar

class Vec2 {
  constructor(x = 0, y = 0) { this.x = x; this.y = y; }
  add(v) { return new Vec2(this.x + v.x, this.y + v.y); }
  sub(v) { return new Vec2(this.x - v.x, this.y - v.y); }
  mul(s) { return new Vec2(this.x * s, this.y * s); }
  len() { return Math.hypot(this.x, this.y); }
  norm() { const l = this.len() || 1; return new Vec2(this.x / l, this.y / l); }
}

const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

class Mouse {
  constructor(id, pos, energyValue) {
    this.id = id;
    this.pos = pos;
    this.energyValue = energyValue;
    this.alive = true;
  }
}

class Cat {
  constructor(pos, speed, energy = 100) {
    this.pos = pos;
    this.speed = speed;
    this.energy = energy;
    this.currentTarget = null;
  }
}

class World {
  constructor({ width = 50, height = 30, nMice = 5, catSpeed = 5, mouseSpeed = 3, catchRadius = 1.0, energyCostPerUnit = 0.5, maxTicks = 50 } = {}) {
    this.width = width;
    this.height = height;
    this.catchRadius = catchRadius;
    this.energyCostPerUnit = energyCostPerUnit;
    this.maxTicks = maxTicks;
    this.cat = new Cat(new Vec2(Math.random() * width, Math.random() * height), catSpeed);

    this.mice = [];
    for (let i = 0; i < nMice; i++) {
      this.mice.push(new Mouse(i, new Vec2(Math.random() * width, Math.random() * height), 20));
    }
  }

  pickBestTarget() {
    let best = null;
    for (const m of this.mice) {
      if (!m.alive) continue;
      const dist = m.pos.sub(this.cat.pos).len();
      if (!best || dist < best.dist) {
        best = { mouse: m, dist };
      }
    }
    this.cat.currentTarget = best ? best.mouse : null;
    return best;
  }

  tick(t) {
    const targetInfo = this.pickBestTarget();
    if (!targetInfo) return { done: true, reason: 'Todos los ratones fueron cazados.' };

    const target = targetInfo.mouse;
    const dist = targetInfo.dist;
    const step = Math.min(this.cat.speed, dist);
    const move = target.pos.sub(this.cat.pos).norm().mul(step);
    this.cat.pos = this.cat.pos.add(move);

    const energyBefore = this.cat.energy;
    this.cat.energy = clamp(this.cat.energy - step * this.energyCostPerUnit, 0, 100);

    console.log(`[TICK ${t}] Distancias a ratones:`);
    for (const m of this.mice) {
      if (m.alive) {
        console.log(`  Ratón #${m.id} -> Distancia: ${m.pos.sub(this.cat.pos).len().toFixed(2)}`);
      }
    }

    if (this.cat.pos.sub(target.pos).len() <= this.catchRadius) {
      target.alive = false;
      const before = this.cat.energy;
      this.cat.energy = clamp(this.cat.energy + target.energyValue, 0, 100);
      console.log(`>>> El gato cazó al ratón #${target.id}! Energía antes: ${before.toFixed(1)}, después: ${this.cat.energy.toFixed(1)}`);
    }

    const alive = this.mice.filter(m => m.alive).length;
    return { done: alive === 0 || t >= this.maxTicks, reason: alive === 0 ? 'Todos cazados.' : (t >= this.maxTicks ? 'Tiempo máximo alcanzado' : null) };
  }
}

function run() {
  const world = new World({ nMice: 5, width: 50, height: 30, maxTicks: 50 });

  for (let t = 1; t <= world.maxTicks; t++) {
    const res = world.tick(t);
    if (res.done) {
      console.log(`Fin: ${res.reason}`);
      break;
    }
  }
}

run();
