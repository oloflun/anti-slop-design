// React Theme — extracted from https://customer.io
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '30': string;
    '36': string;
    '40': string;
    '64': string;
    '96': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '48': string;
    '64': string;
    '80': string;
    '96': string;
    '120': string;
    '128': string;
    '160': string;
 *   };
 *   radii: {
    xs: string;
    md: string;
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
    "primary": "#fff8e9",
    "secondary": "#01090b",
    "accent": "#c3e7ff",
    "background": "#000405",
    "foreground": "#000000",
    "neutral50": "#d4d4d4",
    "neutral100": "#ffffff",
    "neutral200": "#5a8990",
    "neutral300": "#f4f4f4"
  },
  "fonts": {
    "body": "'saansFont', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "30": "30px",
    "36": "36px",
    "40": "40px",
    "64": "64px",
    "96": "96px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "96": "96px",
    "120": "120px",
    "128": "128px",
    "160": "160px"
  },
  "radii": {
    "xs": "2px",
    "md": "6px"
  },
  "shadows": {
    "sm": "oklch(0.97 0 0) 0px 0px 0px 4px"
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
      "main": "#fff8e9",
      "light": "hsl(41, 100%, 95%)",
      "dark": "hsl(41, 100%, 81%)"
    },
    "secondary": {
      "main": "#01090b",
      "light": "hsl(192, 83%, 17%)",
      "dark": "hsl(192, 83%, 10%)"
    },
    "background": {
      "default": "#000405",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#000506"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "600",
      "lineHeight": "40.5px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "475",
      "lineHeight": "27px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "oklch(0.9263 0.136 145.2) 0px 0px 0px 4px",
    "oklch(0.97 0 0) 0px 0px 0px 4px"
  ]
};

export default theme;
