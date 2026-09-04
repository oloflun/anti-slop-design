// React Theme — extracted from https://theequityfund.org
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
    heading: string;
 *   };
 *   fontSizes: {
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '28': string;
    '36': string;
    '60': string;
    '100': string;
    '204.8': string;
    '41.6': string;
 *   };
 *   space: {
    '4': string;
    '64': string;
    '96': string;
    '120': string;
    '144': string;
    '208': string;
    '311': string;
    '329': string;
 *   };
 *   radii: {
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
    "primary": "#c4b3e0",
    "secondary": "#500c20",
    "accent": "#fcf6ed",
    "background": "#fcf6ed",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#000000"
  },
  "fonts": {
    "body": "'Metrify', sans-serif",
    "heading": "'Judge', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "36": "36px",
    "60": "60px",
    "100": "100px",
    "204.8": "204.8px",
    "41.6": "41.6px"
  },
  "space": {
    "4": "4px",
    "64": "64px",
    "96": "96px",
    "120": "120px",
    "144": "144px",
    "208": "208px",
    "311": "311px",
    "329": "329px"
  },
  "radii": {
    "full": "9999px"
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
      "main": "#c4b3e0",
      "light": "hsl(263, 42%, 94%)",
      "dark": "hsl(263, 42%, 64%)"
    },
    "secondary": {
      "main": "#500c20",
      "light": "hsl(342, 74%, 33%)",
      "dark": "hsl(342, 74%, 10%)"
    },
    "background": {
      "default": "#fcf6ed",
      "paper": "#c4b3e0"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#500c20"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "500",
      "lineHeight": "50.4px",
      "fontFamily": "'Judge', sans-serif"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "33.6px",
      "fontFamily": "'Judge', sans-serif"
    }
  },
  "shape": {
    "borderRadius": 9999
  },
  "shadows": []
};

export default theme;
