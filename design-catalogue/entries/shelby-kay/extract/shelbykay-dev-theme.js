// React Theme — extracted from https://shelbykay.dev/
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
    neutral300: string;
    neutral400: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '11': string;
    '14': string;
    '16': string;
    '20': string;
    '24': string;
    '256': string;
    '140.8': string;
    '73.92': string;
 *   };
 *   space: {
    '6': string;
    '35': string;
    '56': string;
    '80': string;
    '112': string;
    '128': string;
    '200': string;
    '248': string;
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
    "primary": "#d6b292",
    "secondary": "#efe6d9",
    "background": "#efe6d9",
    "foreground": "#393c2a",
    "neutral50": "#393c2a",
    "neutral100": "#000000",
    "neutral200": "#737955",
    "neutral300": "#afa199",
    "neutral400": "#7b8785"
  },
  "fonts": {
    "body": "'Ranade', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "11": "11px",
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "256": "256px",
    "140.8": "140.8px",
    "73.92": "73.92px"
  },
  "space": {
    "6": "6px",
    "35": "35px",
    "56": "56px",
    "80": "80px",
    "112": "112px",
    "128": "128px",
    "200": "200px",
    "248": "248px"
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
      "main": "#d6b292",
      "light": "hsl(28, 45%, 86%)",
      "dark": "hsl(28, 45%, 56%)"
    },
    "secondary": {
      "main": "#efe6d9",
      "light": "hsl(35, 41%, 95%)",
      "dark": "hsl(35, 41%, 74%)"
    },
    "background": {
      "default": "#efe6d9",
      "paper": "#000000"
    },
    "text": {
      "primary": "#393c2a",
      "secondary": "#737955"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "73.92px",
      "fontWeight": "700",
      "lineHeight": "73.92px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "700",
      "lineHeight": "28.8px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "24px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "600",
      "lineHeight": "20px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
