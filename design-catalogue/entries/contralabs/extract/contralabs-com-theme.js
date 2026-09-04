// React Theme — extracted from https://contralabs.com
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
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '44': string;
    '56': string;
    '62': string;
    '64': string;
    '268': string;
    '597.662': string;
    '354.9': string;
    '328.936': string;
    '316.339': string;
    '311.21': string;
    '228.851': string;
    '135.252': string;
 *   };
 *   space: {
    '1': string;
    '30': string;
    '40': string;
    '48': string;
    '60': string;
    '74': string;
    '80': string;
    '100': string;
    '120': string;
    '160': string;
    '184': string;
    '200': string;
 *   };
 *   radii: {
    md: string;
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
    "primary": "#fbfaf6",
    "secondary": "#0000ee",
    "accent": "#f50c0c",
    "background": "#fbfaf6",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#2b2b29",
    "neutral200": "#a5beba",
    "neutral300": "#494444",
    "neutral400": "#918f66",
    "neutral500": "#918989",
    "neutral600": "#c8bcae",
    "neutral700": "#e4e2d9",
    "neutral800": "#83a5a0"
  },
  "fonts": {
    "body": "'GT Standard L Medium', sans-serif"
  },
  "fontSizes": {
    "44": "44px",
    "56": "56px",
    "62": "62px",
    "64": "64px",
    "268": "268px",
    "597.662": "597.662px",
    "354.9": "354.9px",
    "328.936": "328.936px",
    "316.339": "316.339px",
    "311.21": "311.21px",
    "228.851": "228.851px",
    "135.252": "135.252px"
  },
  "space": {
    "1": "1px",
    "30": "30px",
    "40": "40px",
    "48": "48px",
    "60": "60px",
    "74": "74px",
    "80": "80px",
    "100": "100px",
    "120": "120px",
    "160": "160px",
    "184": "184px",
    "200": "200px"
  },
  "radii": {
    "md": "8px",
    "xl": "24px",
    "full": "10000px"
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
      "main": "#fbfaf6",
      "light": "hsl(48, 38%, 95%)",
      "dark": "hsl(48, 38%, 82%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#fbfaf6",
      "paper": "#c8e1dd"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#2b2b29"
    }
  },
  "typography": {
    "fontFamily": "'GT Standard L Regular', sans-serif",
    "h1": {
      "fontSize": "268px",
      "fontWeight": "400",
      "lineHeight": "241.2px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;
