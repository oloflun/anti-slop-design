// React Theme — extracted from http://127.0.0.1:3055/sites/horai.html
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
 *   };
 *   fontSizes: {
    '114': string;
    '192': string;
    '89.6': string;
    '81.92': string;
    '71.68': string;
    '58.88': string;
    '51.2': string;
    '46.08': string;
    '35.84': string;
    '34.2': string;
    '28.5': string;
    '28.16': string;
 *   };
 *   space: {
    '10': string;
    '57': string;
    '67': string;
    '114': string;
    '152': string;
    '190': string;
    '209': string;
    '410': string;
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
    "primary": "#650001",
    "secondary": "#06190f",
    "accent": "#e0cbab",
    "background": "#e0cbab",
    "foreground": "#040202",
    "neutral50": "#e5e7eb",
    "neutral100": "#040202",
    "neutral200": "#1e1513"
  },
  "fonts": {
    "body": "'Noto Serif JP', sans-serif"
  },
  "fontSizes": {
    "114": "114px",
    "192": "192px",
    "89.6": "89.6px",
    "81.92": "81.92px",
    "71.68": "71.68px",
    "58.88": "58.88px",
    "51.2": "51.2px",
    "46.08": "46.08px",
    "35.84": "35.84px",
    "34.2": "34.2px",
    "28.5": "28.5px",
    "28.16": "28.16px"
  },
  "space": {
    "10": "10px",
    "57": "57px",
    "67": "67px",
    "114": "114px",
    "152": "152px",
    "190": "190px",
    "209": "209px",
    "410": "410px"
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
      "main": "#650001",
      "light": "hsl(359, 100%, 35%)",
      "dark": "hsl(359, 100%, 10%)"
    },
    "secondary": {
      "main": "#06190f",
      "light": "hsl(148, 61%, 21%)",
      "dark": "hsl(148, 61%, 10%)"
    },
    "background": {
      "default": "#e0cbab",
      "paper": "#040202"
    },
    "text": {
      "primary": "#040202",
      "secondary": "#efdfcc"
    }
  },
  "typography": {
    "fontFamily": "'Vollkorn', sans-serif",
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
