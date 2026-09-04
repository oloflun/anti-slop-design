// React Theme — extracted from https://www.get-ripe.com/
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
 *   };
 *   fonts: {
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '13': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '32': string;
    '48': string;
    '64': string;
    '72': string;
    '88': string;
    '96': string;
    '128': string;
 *   };
 *   space: {
    '1': string;
    '32': string;
    '37': string;
    '48': string;
    '53': string;
    '61': string;
    '80': string;
    '120': string;
    '160': string;
    '200': string;
 *   };
 *   radii: {
    lg: string;
    xl: string;
    full: string;
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
    "primary": "#0a1714",
    "secondary": "#fff7eb",
    "accent": "#fff8bb",
    "background": "#efe5d4",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#61805b",
    "neutral200": "#ffffff",
    "neutral300": "#767676",
    "neutral400": "#bbd0b7"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif",
    "heading": "'SeriouslyNostalgic Condensed', sans-serif"
  },
  "fontSizes": {
    "13": "13px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "32": "32px",
    "48": "48px",
    "64": "64px",
    "72": "72px",
    "88": "88px",
    "96": "96px",
    "128": "128px"
  },
  "space": {
    "1": "1px",
    "32": "32px",
    "37": "37px",
    "48": "48px",
    "53": "53px",
    "61": "61px",
    "80": "80px",
    "120": "120px",
    "160": "160px",
    "200": "200px"
  },
  "radii": {
    "lg": "16px",
    "xl": "24px",
    "full": "100px"
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
      "main": "#0a1714",
      "light": "hsl(166, 39%, 21%)",
      "dark": "hsl(166, 39%, 10%)"
    },
    "secondary": {
      "main": "#fff7eb",
      "light": "hsl(36, 100%, 95%)",
      "dark": "hsl(36, 100%, 81%)"
    },
    "background": {
      "default": "#efe5d4",
      "paper": "#fff7eb"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0a1714"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "48px",
      "fontWeight": "400",
      "lineHeight": "48px",
      "fontFamily": "'SeriouslyNostalgic Condensed', sans-serif"
    }
  },
  "shape": {
    "borderRadius": 16
  },
  "shadows": []
};

export default theme;
