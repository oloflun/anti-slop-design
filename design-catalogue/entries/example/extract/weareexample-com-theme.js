// React Theme — extracted from https://www.weareexample.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '32': string;
    '64': string;
    '72': string;
    '96': string;
    '230.4': string;
    '184.32': string;
    '182.4': string;
    '166.4': string;
    '140.8': string;
    '102.4': string;
    '38.4': string;
    '35.84': string;
 *   };
 *   space: {
    '1': string;
    '10': string;
    '12': string;
    '24': string;
    '32': string;
    '36': string;
    '38': string;
    '51': string;
    '64': string;
    '80': string;
    '102': string;
    '104': string;
    '126': string;
    '128': string;
    '140': string;
    '192': string;
 *   };
 *   radii: {
    xs: string;
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
    "primary": "#2cc9ff",
    "secondary": "#ff0000",
    "accent": "#ffdede",
    "background": "#f3f3f0",
    "foreground": "#000000",
    "neutral50": "#f3f3f0",
    "neutral100": "#000000",
    "neutral200": "#424242",
    "neutral300": "#1f1f1f",
    "neutral400": "#ffffff",
    "neutral500": "#dddddd",
    "neutral600": "#111111"
  },
  "fonts": {
    "body": "'Menlo', sans-serif"
  },
  "fontSizes": {
    "32": "32px",
    "64": "64px",
    "72": "72px",
    "96": "96px",
    "230.4": "230.4px",
    "184.32": "184.32px",
    "182.4": "182.4px",
    "166.4": "166.4px",
    "140.8": "140.8px",
    "102.4": "102.4px",
    "38.4": "38.4px",
    "35.84": "35.84px"
  },
  "space": {
    "1": "1px",
    "10": "10px",
    "12": "12px",
    "24": "24px",
    "32": "32px",
    "36": "36px",
    "38": "38px",
    "51": "51px",
    "64": "64px",
    "80": "80px",
    "102": "102px",
    "104": "104px",
    "126": "126px",
    "128": "128px",
    "140": "140px",
    "192": "192px"
  },
  "radii": {
    "xs": "2px",
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
      "main": "#2cc9ff",
      "light": "hsl(195, 100%, 74%)",
      "dark": "hsl(195, 100%, 44%)"
    },
    "secondary": {
      "main": "#ff0000",
      "light": "hsl(0, 100%, 65%)",
      "dark": "hsl(0, 100%, 35%)"
    },
    "background": {
      "default": "#f3f3f0",
      "paper": "#f8f8ef"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0e1623"
    }
  },
  "typography": {
    "fontFamily": "'Ppeditorialnew', sans-serif",
    "h1": {
      "fontSize": "102.4px",
      "fontWeight": "900",
      "lineHeight": "81.92px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": []
};

export default theme;
