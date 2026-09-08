// React Theme — extracted from http://127.0.0.1:3055/sites/hyperborea.html
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '17': string;
    '18': string;
    '19': string;
    '24': string;
    '30': string;
    '48': string;
    '60': string;
    '64': string;
    '140.8': string;
    '89.6': string;
    '69.12': string;
    '58.88': string;
 *   };
 *   space: {
    '4': string;
    '48': string;
    '56': string;
    '80': string;
    '96': string;
    '112': string;
    '176': string;
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
    "primary": "#ff5c0b",
    "secondary": "#730405",
    "accent": "#e3d2b8",
    "background": "#000102",
    "foreground": "#e3d2b8",
    "neutral50": "#e5e7eb",
    "neutral100": "#000102"
  },
  "fonts": {
    "body": "'Noto Serif JP', sans-serif"
  },
  "fontSizes": {
    "17": "17px",
    "18": "18px",
    "19": "19px",
    "24": "24px",
    "30": "30px",
    "48": "48px",
    "60": "60px",
    "64": "64px",
    "140.8": "140.8px",
    "89.6": "89.6px",
    "69.12": "69.12px",
    "58.88": "58.88px"
  },
  "space": {
    "4": "4px",
    "48": "48px",
    "56": "56px",
    "80": "80px",
    "96": "96px",
    "112": "112px",
    "176": "176px"
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
      "main": "#ff5c0b",
      "light": "hsl(20, 100%, 67%)",
      "dark": "hsl(20, 100%, 37%)"
    },
    "secondary": {
      "main": "#730405",
      "light": "hsl(359, 93%, 38%)",
      "dark": "hsl(359, 93%, 10%)"
    },
    "background": {
      "default": "#000102",
      "paper": "#010205"
    },
    "text": {
      "primary": "#e3d2b8",
      "secondary": "#000102"
    }
  },
  "typography": {
    "fontFamily": "'Archivo', sans-serif",
    "h1": {
      "fontSize": "58.88px",
      "fontWeight": "400",
      "lineHeight": "58.88px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
