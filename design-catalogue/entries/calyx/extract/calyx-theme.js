// React Theme — extracted from http://127.0.0.1:3055/sites/calyx.html
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '15': string;
    '16': string;
    '17': string;
    '24': string;
    '30': string;
    '36': string;
    '88': string;
    '115.2': string;
    '89.6': string;
    '53.76': string;
    '51.2': string;
    '10.5': string;
 *   };
 *   space: {
    '4': string;
    '96': string;
    '112': string;
 *   };
 *   radii: {

 *   };
 *   shadows: {

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
    "primary": "#400d05",
    "secondary": "#ede5d3",
    "background": "#ede5d3",
    "foreground": "#020201",
    "neutral50": "#e5e7eb",
    "neutral100": "#020201",
    "neutral200": "#191915"
  },
  "fonts": {
    "body": "'Cardo', sans-serif",
    "mono": "'PT Mono', monospace"
  },
  "fontSizes": {
    "15": "15px",
    "16": "16px",
    "17": "17px",
    "24": "24px",
    "30": "30px",
    "36": "36px",
    "88": "88px",
    "115.2": "115.2px",
    "89.6": "89.6px",
    "53.76": "53.76px",
    "51.2": "51.2px",
    "10.5": "10.5px"
  },
  "space": {
    "4": "4px",
    "96": "96px",
    "112": "112px"
  },
  "radii": {},
  "shadows": {},
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
      "main": "#400d05",
      "light": "hsl(8, 86%, 29%)",
      "dark": "hsl(8, 86%, 10%)"
    },
    "secondary": {
      "main": "#ede5d3",
      "light": "hsl(42, 42%, 95%)",
      "dark": "hsl(42, 42%, 73%)"
    },
    "background": {
      "default": "#ede5d3",
      "paper": "#020201"
    },
    "text": {
      "primary": "#020201",
      "secondary": "#191915"
    }
  },
  "typography": {
    "fontFamily": "'PT Mono', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "40px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
