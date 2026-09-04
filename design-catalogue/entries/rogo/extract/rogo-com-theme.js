// React Theme — extracted from https://rogo.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
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
    '24': string;
    '28': string;
    '44': string;
    '48': string;
    '64': string;
    '96': string;
 *   };
 *   space: {
    '1': string;
    '108': string;
    '120': string;
    '164': string;
    '196': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#0000ee",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#151515",
    "neutral300": "#737373",
    "neutral400": "#eeedec",
    "neutral500": "#383838",
    "neutral600": "#444444"
  },
  "fonts": {
    "body": "'ABC Arizona Mix Regular', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "44": "44px",
    "48": "48px",
    "64": "64px",
    "96": "96px"
  },
  "space": {
    "1": "1px",
    "108": "108px",
    "120": "120px",
    "164": "164px",
    "196": "196px"
  },
  "radii": {
    "md": "6px"
  },
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
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#737373"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "44px",
      "fontWeight": "400",
      "lineHeight": "46.2px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "500",
      "lineHeight": "26.4px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": []
};

export default theme;
