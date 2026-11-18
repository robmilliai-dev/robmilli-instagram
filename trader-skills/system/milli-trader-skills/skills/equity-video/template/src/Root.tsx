import React from "react";
import { Composition } from "remotion";
import { EquityCurve, type EquityProps } from "./EquityCurve";

// Presets: reel (1080x1920), square (1080x1080), wide (1920x1080). 30 fps.
const PRESETS = {
  reel: { width: 1080, height: 1920 },
  square: { width: 1080, height: 1080 },
  wide: { width: 1920, height: 1080 },
} as const;

const sample: EquityProps = {
  title: "Trend rule on SPY",
  subtitle: "Backtest 2015 to 2025 · costs included",
  hook: "10 years. One rule. Here's every drop.",
  points: Array.from({ length: 120 }, (_, i) => 10000 * Math.pow(1.006, i) * (1 + 0.05 * Math.sin(i / 7))),
  startLabel: "2015",
  endLabel: "2025",
  footer: "Backtest, not live results. Not financial advice. milli-ai.com",
  preset: "reel",
  accent: "#22d3a6",
};

export const Root: React.FC = () => (
  <>
    {(Object.keys(PRESETS) as (keyof typeof PRESETS)[]).map((k) => (
      <Composition
        key={k}
        id={k === "reel" ? "EquityCurve" : `EquityCurve-${k}`}
        component={EquityCurve}
        durationInFrames={360}
        fps={30}
        width={PRESETS[k].width}
        height={PRESETS[k].height}
        defaultProps={{ ...sample, preset: k }}
      />
    ))}
  </>
);
