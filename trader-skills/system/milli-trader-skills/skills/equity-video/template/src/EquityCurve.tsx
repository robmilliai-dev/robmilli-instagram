import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig, Easing } from "remotion";

export type EquityProps = {
  title: string;
  subtitle: string;
  hook: string;
  points: number[];
  benchmark?: number[];
  benchmarkLabel?: string;
  startLabel: string;
  endLabel: string;
  footer: string;
  preset: "reel" | "square" | "wide";
  accent: string;
};

const BG = "#0b0f14";
const INK = "#f4f6f8";
const MUTED = "#8b97a6";
const RED = "#ff5c6c";

function maxDrawdown(p: number[]) {
  let peak = p[0], worst = 0, at = 0;
  p.forEach((v, i) => { peak = Math.max(peak, v); const dd = v / peak - 1; if (dd < worst) { worst = dd; at = i; } });
  return { worst, at };
}

function path(vals: number[], n: number, x0: number, y0: number, w: number, h: number, lo: number, hi: number) {
  const k = Math.max(2, Math.floor(n));
  return vals.slice(0, k).map((v, i) => {
    const x = x0 + (i / (vals.length - 1)) * w;
    const y = y0 + h - ((v - lo) / (hi - lo)) * h;
    return `${i ? "L" : "M"}${x.toFixed(1)},${y.toFixed(1)}`;
  }).join(" ");
}

export const EquityCurve: React.FC<EquityProps> = (p) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const pad = width * 0.08;
  const chartTop = height * (p.preset === "reel" ? 0.3 : 0.28);
  const chartH = height * (p.preset === "reel" ? 0.42 : 0.5);
  const chartW = width - pad * 2;
  const all = [...p.points, ...(p.benchmark ?? [])];
  const lo = Math.min(...all) * 0.97, hi = Math.max(...all) * 1.03;

  // 0-1.5s hook, 1.5-8s draw, 8-12s stats
  const hookIn = spring({ frame, fps, config: { damping: 200 } });
  const draw = interpolate(frame, [45, 240], [0, p.points.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.inOut(Easing.cubic) });
  const statsIn = spring({ frame: frame - 245, fps, config: { damping: 200 } });

  const total = p.points[p.points.length - 1] / p.points[0] - 1;
  const bench = p.benchmark ? p.benchmark[p.benchmark.length - 1] / p.benchmark[0] - 1 : null;
  const dd = maxDrawdown(p.points);
  const shown = Math.max(1, Math.floor(draw));
  const liveRet = p.points[Math.min(shown, p.points.length) - 1] / p.points[0] - 1;
  const fmt = (x: number) => `${x >= 0 ? "+" : ""}${(x * 100).toFixed(0)}%`;
  const big = width * (p.preset === "wide" ? 0.05 : 0.075);

  const ddX = pad + (dd.at / (p.points.length - 1)) * chartW;
  const ddY = chartTop + chartH - ((p.points[dd.at] - lo) / (hi - lo)) * chartH;
  const ddVisible = draw >= dd.at;

  return (
    <AbsoluteFill style={{ backgroundColor: BG, fontFamily: "Inter, Helvetica, Arial, sans-serif", color: INK }}>
      <div style={{ position: "absolute", top: height * 0.07, left: pad, right: pad, opacity: hookIn, transform: `translateY(${(1 - hookIn) * 40}px)` }}>
        <div style={{ fontSize: big, fontWeight: 800, lineHeight: 1.05 }}>{p.hook}</div>
        <div style={{ fontSize: big * 0.38, color: MUTED, marginTop: big * 0.3 }}>{p.title} · {p.subtitle}</div>
      </div>

      <svg width={width} height={height} style={{ position: "absolute", inset: 0 }}>
        {p.benchmark && (
          <path d={path(p.benchmark, draw, pad, chartTop, chartW, chartH, lo, hi)} stroke={MUTED} strokeWidth={width * 0.004} fill="none" strokeDasharray="10 10" />
        )}
        <path d={path(p.points, draw, pad, chartTop, chartW, chartH, lo, hi)} stroke={p.accent} strokeWidth={width * 0.008} fill="none" strokeLinejoin="round" strokeLinecap="round" />
        {ddVisible && (
          <g opacity={interpolate(draw - dd.at, [0, 6], [0, 1], { extrapolateRight: "clamp" })}>
            <circle cx={ddX} cy={ddY} r={width * 0.014} fill={RED} />
            <line x1={ddX} y1={ddY} x2={ddX} y2={chartTop + chartH + width * 0.012} stroke={RED} strokeWidth={2} strokeDasharray="6 6" />
            <text
              x={Math.min(Math.max(ddX, pad + width * 0.16), pad + chartW - width * 0.16)}
              y={chartTop + chartH + width * 0.05}
              fill={RED} fontSize={width * 0.035} fontWeight={700} textAnchor="middle">worst drop {fmt(dd.worst)}</text>
          </g>
        )}
        <text x={pad} y={chartTop + chartH + width * 0.09} fill={MUTED} fontSize={width * 0.03}>{p.startLabel}</text>
        <text x={pad + chartW} y={chartTop + chartH + width * 0.09} fill={MUTED} fontSize={width * 0.03} textAnchor="end">{p.endLabel}</text>
      </svg>

      <div style={{ position: "absolute", top: chartTop - big * 1.2, right: pad, fontSize: big * 0.8, fontWeight: 800, color: liveRet >= 0 ? p.accent : RED }}>
        {fmt(liveRet)}
      </div>

      <div style={{ position: "absolute", top: chartTop + chartH + height * 0.06, left: pad, right: pad, opacity: statsIn, transform: `translateY(${(1 - statsIn) * 30}px)`, display: "flex", gap: pad * 0.5, flexWrap: "wrap" }}>
        {[
          ["Total", fmt(total), p.accent],
          ["Worst drop", fmt(dd.worst), RED],
          ...(bench !== null ? [[p.benchmarkLabel ?? "Benchmark", fmt(bench), MUTED]] : []),
        ].map(([label, value, color]) => (
          <div key={label} style={{ flex: 1, minWidth: chartW * 0.28 }}>
            <div style={{ fontSize: big * 0.35, color: MUTED }}>{label}</div>
            <div style={{ fontSize: big * 0.85, fontWeight: 800, color }}>{value}</div>
          </div>
        ))}
      </div>

      <div style={{ position: "absolute", bottom: height * 0.04, left: pad, right: pad, fontSize: width * 0.024, color: MUTED }}>{p.footer}</div>
    </AbsoluteFill>
  );
};
