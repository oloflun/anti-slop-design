// React Theme — extracted from http://127.0.0.1:3055/sites/before-ai-slop.html
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '30': string;
    '36': string;
    '48': string;
    '60': string;
 *   };
 *   space: {
    '2': string;
    '40': string;
    '48': string;
    '64': string;
    '80': string;
    '96': string;
    '128': string;
    '216': string;
    '264': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#0f172a",
    "secondary": "#059669",
    "accent": "#6366f1",
    "background": "#fbfaf7",
    "foreground": "#1f2937",
    "neutral50": "#e5e7eb",
    "neutral100": "#ffffff",
    "neutral200": "#475569",
    "neutral300": "#64748b",
    "neutral400": "#94a3b8",
    "neutral500": "#eef2ff",
    "neutral600": "#334155",
    "neutral700": "#ecfdf5"
  },
  "fonts": {
    "body": "'Inter', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "30": "30px",
    "36": "36px",
    "48": "48px",
    "60": "60px"
  },
  "space": {
    "2": "2px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "128": "128px",
    "216": "216px",
    "264": "264px"
  },
  "radii": {
    "md": "8px",
    "lg": "16px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#0f172a",
      "light": "hsl(222, 47%, 26%)",
      "dark": "hsl(222, 47%, 10%)"
    },
    "secondary": {
      "main": "#059669",
      "light": "hsl(161, 94%, 45%)",
      "dark": "hsl(161, 94%, 15%)"
    },
    "background": {
      "default": "#fbfaf7",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#1f2937",
      "secondary": "#475569"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "700",
      "lineHeight": "40px"
    },
    "h2": {
      "fontSize": "30px",
      "fontWeight": "700",
      "lineHeight": "36px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "600",
      "lineHeight": "28px"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "400",
      "lineHeight": "29.25px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px"
  ]
};

export default theme;
