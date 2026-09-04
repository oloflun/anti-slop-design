// React Theme — extracted from https://rre.com/
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
    '12': string;
    '15': string;
    '16': string;
    '20': string;
    '24': string;
    '32': string;
    '56': string;
    '80': string;
 *   };
 *   space: {
    '1': string;
    '48': string;
    '78': string;
    '96': string;
    '128': string;
    '200': string;
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
    "primary": "#3898ec",
    "secondary": "#07020a",
    "accent": "#6ccfff",
    "background": "#07020a",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#333333",
    "neutral200": "#cccccc"
  },
  "fonts": {
    "body": "'webflow-icons', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "15": "15px",
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "32": "32px",
    "56": "56px",
    "80": "80px"
  },
  "space": {
    "1": "1px",
    "48": "48px",
    "78": "78px",
    "96": "96px",
    "128": "128px",
    "200": "200px"
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
      "main": "#3898ec",
      "light": "hsl(208, 83%, 72%)",
      "dark": "hsl(208, 83%, 42%)"
    },
    "secondary": {
      "main": "#07020a",
      "light": "hsl(278, 67%, 17%)",
      "dark": "hsl(278, 67%, 10%)"
    },
    "background": {
      "default": "#07020a",
      "paper": "#d3e7f1"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'webflow-icons', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "38.4px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "33.6px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "28px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
