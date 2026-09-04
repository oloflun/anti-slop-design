// React Theme — extracted from https://indoek.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '20': string;
    '24': string;
    '28': string;
    '34': string;
    '40': string;
    '64': string;
 *   };
 *   space: {
    '4': string;
    '80': string;
    '101': string;
    '130': string;
    '144': string;
    '163': string;
    '185': string;
    '208': string;
    '273': string;
 *   };
 *   radii: {
    md: string;
    full: string;
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
    "primary": "#135eab",
    "background": "#efebe3",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#000000",
    "neutral200": "#ffffff"
  },
  "fonts": {
    "body": "'GTStandard-M', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "34": "34px",
    "40": "40px",
    "64": "64px"
  },
  "space": {
    "4": "4px",
    "80": "80px",
    "101": "101px",
    "130": "130px",
    "144": "144px",
    "163": "163px",
    "185": "185px",
    "208": "208px",
    "273": "273px"
  },
  "radii": {
    "md": "8px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 1000px inset"
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
      "main": "#135eab",
      "light": "hsl(210, 80%, 52%)",
      "dark": "hsl(210, 80%, 22%)"
    },
    "background": {
      "default": "#efebe3",
      "paper": "#135eab"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#135eab"
    }
  },
  "typography": {
    "fontFamily": "'GTStandard-M', sans-serif",
    "h1": {
      "fontSize": "34px",
      "fontWeight": "400",
      "lineHeight": "34px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "28.8px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "700",
      "lineHeight": "28px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 1000px inset"
  ]
};

export default theme;
