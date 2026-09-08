// React Theme — extracted from http://127.0.0.1:3055/sites/vintergatan.html
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
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '20': string;
    '24': string;
    '30': string;
    '36': string;
    '153.6': string;
    '121.6': string;
    '89.6': string;
    '70.4': string;
    '53.76': string;
    '51.2': string;
    '43.52': string;
    '17.5': string;
 *   };
 *   space: {
    '4': string;
    '40': string;
    '48': string;
    '56': string;
    '64': string;
    '80': string;
    '96': string;
    '128': string;
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
    "primary": "#3b0604",
    "secondary": "#751510",
    "accent": "#e7dec4",
    "background": "#e7dec4",
    "foreground": "#040201",
    "neutral50": "#e5e7eb",
    "neutral100": "#040201",
    "neutral200": "#1c1611"
  },
  "fonts": {
    "body": "'Cormorant Garamond', sans-serif",
    "mono": "'IBM Plex Mono', monospace"
  },
  "fontSizes": {
    "20": "20px",
    "24": "24px",
    "30": "30px",
    "36": "36px",
    "153.6": "153.6px",
    "121.6": "121.6px",
    "89.6": "89.6px",
    "70.4": "70.4px",
    "53.76": "53.76px",
    "51.2": "51.2px",
    "43.52": "43.52px",
    "17.5": "17.5px"
  },
  "space": {
    "4": "4px",
    "40": "40px",
    "48": "48px",
    "56": "56px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "128": "128px"
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
      "main": "#3b0604",
      "light": "hsl(2, 87%, 27%)",
      "dark": "hsl(2, 87%, 10%)"
    },
    "secondary": {
      "main": "#751510",
      "light": "hsl(3, 76%, 41%)",
      "dark": "hsl(3, 76%, 11%)"
    },
    "background": {
      "default": "#e7dec4",
      "paper": "#040202"
    },
    "text": {
      "primary": "#040201",
      "secondary": "#1c1611"
    }
  },
  "typography": {
    "fontFamily": "'EB Garamond', sans-serif",
    "h1": {
      "fontSize": "51.2px",
      "fontWeight": "400",
      "lineHeight": "53.76px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
