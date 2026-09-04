// React Theme — extracted from https://miti-navi.com/fr
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
    mono: string;
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '26': string;
    '46': string;
    '72': string;
    '80': string;
    '90': string;
    '100': string;
    '110': string;
    '130': string;
    '180': string;
 *   };
 *   space: {
    '5': string;
    '30': string;
    '40': string;
    '60': string;
    '90': string;
    '140': string;
    '240': string;
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
    "primary": "#000e13",
    "secondary": "#ffdead",
    "accent": "#e6dece",
    "background": "#e8ded0",
    "foreground": "#232323",
    "neutral50": "#232323",
    "neutral100": "#999999",
    "neutral200": "#000000",
    "neutral300": "#808080"
  },
  "fonts": {
    "mono": "'GT Pressura Mono', monospace",
    "body": "'Voyage', sans-serif",
    "heading": "'GTSectraDisplay', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "26": "26px",
    "46": "46px",
    "72": "72px",
    "80": "80px",
    "90": "90px",
    "100": "100px",
    "110": "110px",
    "130": "130px",
    "180": "180px"
  },
  "space": {
    "5": "5px",
    "30": "30px",
    "40": "40px",
    "60": "60px",
    "90": "90px",
    "140": "140px",
    "240": "240px"
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
      "main": "#000e13",
      "light": "hsl(196, 100%, 19%)",
      "dark": "hsl(196, 100%, 10%)"
    },
    "secondary": {
      "main": "#ffdead",
      "light": "hsl(36, 100%, 95%)",
      "dark": "hsl(36, 100%, 69%)"
    },
    "background": {
      "default": "#e8ded0",
      "paper": "#e6dece"
    },
    "text": {
      "primary": "#232323",
      "secondary": "#000e13"
    }
  },
  "typography": {
    "fontFamily": "'GT Pressura Mono', sans-serif",
    "h1": {
      "fontSize": "80px",
      "fontWeight": "400",
      "lineHeight": "112px",
      "fontFamily": "'GTSectraDisplay', sans-serif"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
